# This file is part of CAT-SOOP
# Copyright (c) 2011-2014 Massachusetts Institute of Technology
# Copyright (c) 2014-2016 Adam Hartz <hartz@mit.edu>
# Copyright (c) 2017 Joe Steinmeyer <jodalyst@mit.edu>
# CAT-SOOP is licensed under the Affero General Public License, version 1
# See LICENSE file, or http://affero.org/oagpl.html

import os
import re
from base64 import b64encode
import json


def html_format(string):
    s = string.replace('&', '&amp;').replace('<', '&lt;').replace(
        '>', '&gt;').replace('\t', '    ').splitlines(False)
    jx = 0
    for ix, line in enumerate(s):
        for jx, char in enumerate(line):
            if char != ' ':
                break
        s[ix] = '&nbsp;' * jx + line[jx:]

    return '<br>'.join(s)


defaults = {
    'csq_input_check': lambda x: None,
    'csq_code_pre': '',
    'csq_code_post': '',
    'csq_initial': 'int x = 8;',
    'csq_soln': 'int x = 8;',
    'csq_tests': [],
    'csq_log_keypresses': True,
    'csq_variable_blacklist': [],
    'csq_import_blacklist': [],
    'csq_cpu_limit': 2,
    'csq_nproc_limit': 0,
    'csq_memory_limit': 32e6,
    'csq_interface': 'ace',
    'csq_rows': 14,
    'csq_font_size': 16,
}

test_defaults = {
    'npoints': 1,
    'code': "int ans = x;",
    'variable': 'ans',
    'format': '%d',
    'description': '',
    'include': False,
    'include_soln': False,
    'include_description': False,
    'grade': True,
    'show_description': True,
    'show_code': True,
    'check_function': lambda sub, soln: (sub == soln != '') * 1.0,
    'transform_output': lambda x: '<tt>%s</tt>' % (html_format(x), ),
    'show_code': True,
    'show_description': True
}

DEFAULT_COMPILE_OPTIONS = {
    'CPUTIME': 5,
    'CLOCKTIME': 5,
    'MEMORY': 32 * 1024 ** 4,
    'FILESIZE': 1024*1024*1024,
    'FILES':[],# [['copy', '/tmp/cpp_sandbox/WString.h', 'WString.h'],['copy', '/tmp/cpp_sandbox/WString.cpp', 'WString.cpp']],
    'STDIN': '',
}

DEFAULT_RUN_OPTIONS = {
    'CPUTIME': 1,
    'CLOCKTIME': 1,
    'MEMORY': 32 * 1024 ** 2,
    'FILESIZE': 0,
    'BADIMPORT': [],
    'BADVAR': [],
    'FILES': [],
    'STDIN': '',
}

def _mainer(tc, tv, tf):
    return r"""int main() {
    %s
    printf("!LOGOUTPUT(o_O)!\n");
    printf("%s\n", %s);
    return 0;
}""" % (tc, tf, tv)

def _make_test_code(info, code, test):
    c = "#include <stdio.h>\n"
    c += '\n'.join([info['csq_code_pre'], code.replace('\r\n','\n'),
                    info['csq_code_post'], _mainer(test['code'],
                                               test['variable'],
                                               test['format'])])
    return c + '\n'


def total_points(**info):
    bak = info['csq_tests']
    info['csq_tests'] = []
    for i in bak:
        info['csq_tests'].append(dict(test_defaults))
        info['csq_tests'][-1].update(i)
    return sum(i['npoints'] for i in info['csq_tests'])


def _interpret_result(out, err):
    n = out.split("!LOGOUTPUT(o_O)!")
    if len(n) == 2:  # should be this
        out, log = n
    elif len(n) == 1:  # code didn't run to completion
        if err.strip() == "":
            err = ("Your code did not run to completion, "
                   "but no error message was returned."
                   "\nThis normally means that your code contains an "
                   "infinite loop or otherwise took too long to run.")
        log = ''
    else:  # ???
        out = ''
        log = ''
        err = "BAD CODE - this will be logged"
    if len(out) >= 5000:
        out = out[:5000] + "\n\n...OUTPUT TRUNCATED..."

    return (out.strip(), err.strip(), log.strip())


def handle_submission(submissions, **info):
    base = os.path.join(info['cs_data_root'],'courses',info['cs_course'],
                                '__QTYPES__', 'cpp',
                                'sandbox.py')
    exec(open(base).read(), info)
    code = submissions[info['csq_name']]
    if info['csq_interface'] == 'upload':
        e = {}
        code = csm_data_uri.DataURI(sub[1]).data
    code = code.replace('\r\n', '\n')
    tests = [dict(test_defaults) for i in info['csq_tests']]
    for (i, j) in zip(tests, info['csq_tests']):
        i.update(j)

    inp = info['csq_input_check'](code)
    if inp is not None:
        msg = ('<div class="response">'
               '<font color="red">%s</font>'
               '</div>') % inp
        return {'score':0, 'msg':msg}

    bak = info['csq_tests']
    info['csq_tests'] = []
    for i in bak:
        new = dict(test_defaults)
        new.update(i)
        if new['grade']:
            info['csq_tests'].append(new)

    score = 0
    msg = ('\n<br/><button onclick="$(\'#%s_result_showhide\').toggle()">'
           'Show/Hide Detailed Results</button>') % info['csq_name']
    msg += ('<div class="response" id="%s_result_showhide" '
            'style="display:none"><h2>Test Results:</h2>') % info['csq_name']
    count = 1
    for test in info['csq_tests']:
        _code = _make_test_code(info, code, test)


        if 'cached_result' in test:
            log_s = repr(test['cached_result'])
            err_s = 'Loaded cached result'
        else:
            _s_code = _make_test_code(info, info['csq_soln'], test)

            s_n, s_o, s_e, s_r = info['compile_code'](info, _s_code, DEFAULT_COMPILE_OPTIONS)
            if s_r != 0:
                out_s = s_o
                log_s = ''
                err_s = "Our code failed to compile (return code %s):\n%s" % (s_r, s_e)
            else:
                s_o, s_e, s_r = info['run_code'](info, s_n, DEFAULT_RUN_OPTIONS)
                out_s, err_s, log_s = _interpret_result(s_o, s_e)


        n, o, e, r = info['compile_code'](info, _code, DEFAULT_COMPILE_OPTIONS)
        if r != 0:
            out = o
            log = ''
            err = "Your code failed to compile (return code %s):\n%s" % (r, e)
        else:
            o, e, r = info['run_code'](info, n, DEFAULT_RUN_OPTIONS)
            out, err, log = _interpret_result(o, e)

        if count != 1:
            msg += "\n\n<p><hr><p>\n\n"
        msg += "\n<center><h3>Test %02d</h3>" % count
        if test['show_description']:
            msg += "\n<i>%s</i></center><p>" % test['description']

        if test['show_code']:
            coddo = test.get('description','')
            if coddo == '':
                html_code = html_format(test['code'])
            else:
                html_code = html_format(coddo)
            msg += "\nThe test case was:<br>\n<tt>%s</tt>" % html_code

        try:
            percentage = test['check_function'](log, log_s)
        except:
            percentage = 0.0
        imfile = None
        if percentage == 1.0:
            imfile = "check.png"
        elif percentage == 0.0:
            imfile = "cross.png"

        score += percentage * test['npoints']

        if imfile is None:
            image = ''
        else:
            image = "<img src='BASE/images/%s' />" % imfile

        if log_s != '':  # Our solution ran successfully
            msg += ("\n<p>Our solution produced the following "
                    "value for <tt>%s</tt>:") % test['variable']
            m = test['transform_output'](log_s)
            msg += "\n<br><font color='blue'>%s</font>" % m
        else:
            msg += "\n<p><b>OOPS!</b> Our code produced an error:"
            e = html_format(err_s)
            msg += "\n<br><font color='red'><tt>%s</tt></font>" % e

        if log != '':
            msg += ("\n<p>Your submission produced the following "
                    "value for <tt>%s</tt>:") % test['variable']
            m = test['transform_output'](log)
            msg += "\n<br><font color='blue'>%s</font>%s" % (m, image)

        if out != '':
            msg += "\n<p>Your code produced the following output:"
            msg += "<br><pre>%s</pre>" % html_format(out)

        if err != '':
            msg += "\n<p>Your submission produced an error:"
            e = html_format(err)
            msg += "\n<br><font color='red'><tt>%s</tt></font>" % e

        count += 1

    msg += "\n</div>"
    tp = total_points(**info)
    overall = float(score) / tp if tp != 0 else 0
    msg = (('\n<br/>&nbsp;Your score on your most recent '
            'submission was: %01.02f%%') % (overall * 100)) + msg
    return {'score': overall, 'msg':msg}


def make_initial_display(info):
    return info['csq_initial']


def render_html_textarea(last_log, **info):
    return tutor.question('bigbox')[0]['render_html'](last_log, **info)


def render_html_upload(last_log, **info):
    name = info['csq_name']
    init = last_log.get(name, info['csq_initial'])
    params = {
        'name': name,
        'init': str(init),
        'safeinit': init.replace('<', '&lt;'),
        'b64init': b64encode(info['csq_initial']),
        'dl': (' download="%s"' % info['csq_skeleton_name'])
        if 'csq_skeleton_name' in info else 'download'
    }
    out = ''
    if info.get('show_skeleton', True):
        out += ('''<a href="data:text/plain;base64,%(b64init)s" '''
                '''target="_blank"%(dl)s>Code Skeleton</a><br />''') % params
    if last_log.get(name, None) is not None:
        code = last_log[name]
        out += ('''<a href="%s" '''
                '''target="_blank" id="%s_lastfile">'''
                '''Your Last Submission</a><br />''') % (code[1], name)
    out += '''<input type="file" id=%(name)s name="%(name)s" />''' % params
    return out


def render_html_ace(last_log, **info):
    name = info['csq_name']
    init = last_log.get(name, None)
    if init is None:
        init = make_initial_display(info)
    init = str(init.encode('utf-8', 'replace').decode('ascii', 'ignore'))
    fontsize = info['csq_font_size']
    params = {
        'name': name,
        'init': init,
        'safeinit': init.replace('<', '&lt;'),
        'height': info['csq_rows']*(fontsize+4),
        'fontsize': fontsize,
    }

    return '''
<div class="ace_editor_wrapper" id="container%(name)s">
<div id="editor%(name)s" name="editor%(name)s" class="embedded_ace_code">%(safeinit)s</div></div>
<input type="hidden" name="%(name)s" id="%(name)s" />
<input type="hidden" name="%(name)s_log" id="%(name)s_log" />
<script type="text/javascript" src="https://cdn.jsdelivr.net/ace/1.2.6/min/ace.js"></script>
<script type="text/javascript">
    var log%(name)s = new Array();
    var editor%(name)s = ace.edit("editor%(name)s");
    editor%(name)s.setTheme("ace/theme/textmate");
    editor%(name)s.getSession().setMode("ace/mode/c_cpp");
    editor%(name)s.setShowFoldWidgets(false);
    editor%(name)s.setValue(%(init)r)
    $("#%(name)s").val(editor%(name)s.getValue());
    editor%(name)s.on("change",function(e){
        editor%(name)s.getSession().setUseSoftTabs(true);
        $("#%(name)s").val(editor%(name)s.getValue());
    });
    editor%(name)s.clearSelection()
    editor%(name)s.getSession().setUseSoftTabs(true);
    editor%(name)s.on("paste",function(txt){editor%(name)s.getSession().setUseSoftTabs(false);});
    editor%(name)s.getSession().setTabSize(4);
    editor%(name)s.setFontSize("%(fontsize)spx");
    $("#container%(name)s").height(%(height)s);
    $("#editor%(name)s").height(%(height)s);
    editor%(name)s.resize(true);
</script>''' % params


RENDERERS = {
    'textarea': render_html_textarea,
    'ace': render_html_ace,
    'upload': render_html_upload
}


def render_html(last_log, **info):
    renderer = info['csq_interface']
    if renderer in RENDERERS:
        return RENDERERS[renderer](last_log or {}, **info)
    return ("<font color='red'>"
            "Invalid <tt>cpp</tt> interface: %s"
            "</font>") % renderer


def answer_display(**info):
    out = ('Here is the solution we wrote:<p>'
           '<pre>%s</pre>') % html_format(info['csq_soln'])
    return out
