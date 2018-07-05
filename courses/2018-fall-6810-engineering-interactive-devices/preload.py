# LOOK AND FEEL


if 'localhost' in cs_url_root:
    cs_header = '6.810 Engineering Interactive Technologies'
    cs_icon_url = 'COURSE/images/favicon.gif'
    cs_auth_type = 'dummy'
else:
    cs_base_color = "#000000"
    cs_header = '6.810 Engineering Interactive Technologies'
    cs_icon_url = 'COURSE/images/favicon.gif'
cs_long_name = '6.810 Engineering Interactive Technologies'
cs_require_login_to_view = False
csq_always_show_tests = True
csq_allow_check=csq_allow_viewanswer=True
csq_allow_save=False
cs_allow_save=False
allow_save = False
csq_allow_submit = True
#csq_error_on_unknown_variable = True


cs_markdown_ignore_tags = ('metapost', 'mpfig', 'cmpfig', 'script','svg', 'textarea')
cs_content_header = "6.810 Engineering Interactive Technologies"
cs_title = '6.810 Engineering Interactive Technologies'

cs_page_outline_html = ""

"""
                            {'text': 'Ex 02', 'link': 'COURSE/ex02'},
                            {'text': 'Ex 03', 'link': 'COURSE/ex03'},
                            {'text': 'Ex 04', 'link': 'COURSE/ex04'},
                            {'text': 'Ex 05', 'link': 'COURSE/ex05'},
                            {'text': 'Ex 06', 'link': 'COURSE/ex06'},
                            {'text': 'Ex 07', 'link': 'COURSE/ex07'},
                            {'text': 'Ex 08', 'link': 'COURSE/ex08'},
                            {'text': 'Ex 09', 'link': 'COURSE/ex09'},
                            {'text': 'Ex 10', 'link': 'COURSE/ex10'},
                            {'text': 'Ex 11', 'link': 'COURSE/ex11'},
"""

"""

                              {'text': 'Lab 2A', 'link': 'COURSE/lab02a'},
                              {'text': 'Lab 2B', 'link': 'COURSE/lab02b'},
                              {'text': 'Lab 3A', 'link': 'COURSE/lab03a'},
                              {'text': 'Lab 3B', 'link': 'COURSE/lab03b'},
"""


"""
    {'text': 'Information', 'link': [
                                     {'link': 'COURSE/calendar', 'text': 'Calendar and Handouts'},
                                     {'link': 'COURSE/announcements', 'text': 'Archived Announcements'},
                                     'divider',
                                     {'link': 'COURSE/syllabus', 'text': 'Basic Information'},
                                     {'link': 'COURSE/syllabus/staff', 'text': 'Staff Information'},
                                     {'link': 'COURSE/syllabus/collaboration', 'text': 'Collaboration Policy'},
                                     {'link': 'COURSE/syllabus/grading', 'text': 'Grading Policy'},
                                     {'link': 'COURSE/syllabus/responsibilities', 'text': 'Responsibilities'},
                                     'divider',
                                     {'link': 'COURSE/documentation', 'text': 'References and Documentation'},
                                    ]},
"""



cs_template='COURSE/templates/608.template'
cs_theme = 'COURSE/themes/608.css'
# {'link': 'COURSE', 'text': 'Homepage'},
cs_top_menu = [ 
    # {'text': 'Information', 'link': [
    #                                  {'link': 'COURSE/calendar', 'text': 'Calendar and Handouts'},
    #                                  {'link': 'COURSE/announcements', 'text': 'Archived Announcements'},
    #                                  {'link': 'COURSE/syllabus', 'text': 'Course Information'},
    #                                  'divider',
    #                                  {'link': 'COURSE/final_project', 'text': 'Final Project'},
    #                                  'divider',
    #                                  {'link': 'COURSE/documentation', 'text': 'References and Documentation'},
    #                                 ]},
    {'text': 'Slides', 'link': 'COURSE/progress'},
    {'text': 'UI Analysis', 'link': [
                                    {'text': 'Autoshade Sunglasses', 'link': 'COURSE/ui-analyze-autoshade-sunglasses'},
                                    {'text': 'Hangsmart', 'link': 'COURSE/ui-analyze-hangsmart'},
                                    {'text': 'Flat Water Bottle', 'link': 'COURSE/ui-analyze-flat-water-bottle'},
                                    {'text': 'Flying Selfie Camera', 'link': 'COURSE/ui-analyze-flying-selfie-camera'},
                                    {'text': 'Tippen mit Kippen', 'link': 'COURSE/ui-analyze-cigarette-voting'},
                                    {'text': 'Rinser Toothbrush', 'link': 'COURSE/ui-analyze-rinser-toothbrush'},
                                    {'text': 'Zipzshoes', 'link': 'COURSE/ui-analyze-zipz-shoes'},
                                    ]},
    {'text': 'Group Project', 'link': 'COURSE/progress'},
    {'text': 'Homework', 'link': [{'text': 'Lasercut Businesscard (Due: 9/26/2018)', 'link': 'COURSE/hw-lasercut-business-card'},
                            {'text': 'Ex 02 (Due: 6/28/2018)', 'link': 'COURSE/ex02'},
                            {'text': 'Ex 03 (Due: 7/01/2018)', 'link': 'COURSE/ex03'},
                            {'text': 'Ex 04 (Due: 7/03/2018)', 'link': 'COURSE/ex04'},
                            {'text': 'Ex 05 (Due: 7/05/2018)', 'link': 'COURSE/ex05'},
                            {'text': 'Ex 06 (Due: 7/08/2018)', 'link': 'COURSE/ex06'},
                            {'text': 'Ex 07 (Due: 7/10/2018)', 'link': 'COURSE/ex07'},
                            {'text': 'Ex 08 (Due: 7/12/2018)', 'link': 'COURSE/ex08'},
                            {'text': 'Ex 09 (Due: 7/15/2018)', 'link': 'COURSE/ex09'},
                                      ]},
    {'text': 'Tutorials', 'link': [{'text': 'Lab 1', 'link': 'COURSE/lab01'},
                              {'text': 'Lab 2', 'link': 'COURSE/lab02'},
                              {'text': 'Lab 3', 'link': 'COURSE/lab03'},
                              {'text': 'Lab 4', 'link': 'COURSE/lab04'},
                              {'text': 'Lab 5', 'link': 'COURSE/lab05'},
                              {'text': 'Lab 6', 'link': 'COURSE/lab06'},
                              {'text': 'Lab 7', 'link': 'COURSE/lab07'},
                              {'text': 'Lab 8', 'link': 'COURSE/lab08'},
                              {'text': 'Lab 9', 'link': 'COURSE/lab09'},
                                    ]}
]



#                                      {'text': 'Progress', 'link': 'COURSE/progress'},
# cs_top_menu = []


# def csq_nsubmits_message(nsub, nused, nleft):
#     return 'You have submitted this assignment %d time%s.' % (nused, '' if nused == 1 else 's')
cs_nsubmits_default = 10
# AUTHENTICATION

# blanket extensions
# Lab 1, q08, ignore for everyone
'''
if '608' in cs_url_root:
    # on the real server, use openid_connect to authenticate
    cs_auth_type="openid_connect"
    cs_openid_server = 'https://oidc.mit.edu'
    cs_openid_client_id = "3b5d3e56-dc38-4ac1-a91b-af05fbb6ba58"
    cs_openid_client_secret = "WgzJnMT3m4d0JvVTqACXrLeEPD6a-CrqGap2tk5E3Gss8Qg1MBKVHmBr8dq6bzW1pPYOTiaNFjIehh8gWmzJsg"
    #cs_openid_client_id = 'c030f3ee-fdd7-4867-964b-b6caa37df183'
    #cs_openid_client_secret = 'DwR94C9SiZUSkK7yIy2f7nKk7TwvgW_FqwYCVdW4csZtQlKlRGW_biJ2clKX8PeD-8fHdOXTb10VTOrzqlfxeg'
    def cs_openid_email_generator(idtoken, userinfo):
        if 'email' in userinfo:
            return userinfo['email']
        elif 'preferred_username' in userinfo:
            return '%s@mit.edu' % userinfo['preferred_username']
        else:
            return 'NO EMAIL'
else:
    # locally, use passwords.
'''
cs_auth_type='login'

cs_breadcrumbs_skip_paths = {'python/installing', 'python/ssh', 'quiz1', 'quiz1_practice2', 'graphs', 'graphs/lab_summary'}  # paths to skip

# custom XML tag handling, copied from one i wrote for 6.01 ages ago.
# can probably largely be ignored.
import re
import hashlib
import subprocess
import shutil
def environment_matcher(tag):
    return re.compile("""<%s>(?P<body>.*?)</%s>""" % (tag, tag), re.MULTILINE|re.DOTALL)
def cs_course_handle_custom_tags(text):
    path = cs_path_info[1:]
    direc = os.path.join(base_context.cs_data_root,'courses',cs_course)
    for ix,i in enumerate(path):
        d = loader.get_directory_name(globals(), cs_course, path[:ix], i)
        if d is None:
            break
        direc = os.path.join(direc, d)
    direc = os.path.join(direc, '__MEDIA__')

    #METAPOST
    METAPOST_REGEX = re.compile("<(?P<type>(?:metapost)|(?:mpfig))>(?P<body>.*?)</(?P=type)>", re.MULTILINE|re.DOTALL)
    mpenv = []

    cmp_regex = re.compile(r"<cmpfig>(?P<body>.*?)</cmpfig>", re.MULTILINE|re.DOTALL)
    text = re.sub(cmp_regex, lambda m: '<center><mpfig>%s</mpfig></center>' % m.groupdict()['body'], text)

    def metapost(match):
        d = match.groupdict()
        t = d['type']
        b = d['body']

        if t == 'metapost':
            mpenv.append(b)
            return ''
        else: #type is mpfig
            #make sure media dir exists
            if not os.path.isdir(direc):
                os.makedirs(direc)

            #construct MP file from current env and this fig
            header = 'verbatimtex %&cont-en\n\\input envMPfigs\netex\ninput defs'
            mptext = '\n'.join([header]+mpenv+[r'beginfig(100)',b,'setbounds currentpicture to boundingbox currentpicture enlarged 1pt;','currentpicture := currentpicture scaled 1.7;','endfig;','end'])

            #use hash get filename
            hsh = hashlib.sha512(mptext.encode()).hexdigest()
            basename = 'catsoop_mpfig_%s.svg' % hsh

            fname = os.path.join(direc,basename)

            if not os.path.isfile(fname):
                #if the file doesn't exist, we need to compile it
                #write to temp file
                mpfname = '/tmp/catsoop_mpfig_%s.mp' % hsh
                f = open(mpfname,'w')
                f.write(mptext)
                f.close()
                args = ['python',os.path.join(base_context.cs_data_root,'courses',cs_course,'_util','mptosvg'),mpfname,hsh]
                #call mptosvg on the source
                p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                subout,suberr = p.communicate(None)
                if p.returncode == 0:
                    if not os.path.isdir(direc):
                        os.mkdir(direc)
                    try:
                        shutil.copy('/tmp/mptosvg%s/mp_100.svg' % hsh,fname)
                    except:
                        return '<font color="red"><b>METAPOST Error</b><br/><textarea>%s</textarea></font>' % subout
                    shutil.rmtree('/tmp/mptosvg%s' % hsh,True)
                    try:
                        os.remove('/tmp/catsoop_mpfig_%s.mp' % hsh)
                    except:
                        pass
                else:
                    return '<font color="red"><b>METAPOST Error:</b><pre>%s</pre></font>' % suberr
            return '<img src="CURRENT/%s" />' % basename
    text = re.sub(METAPOST_REGEX, metapost, text)

    # CHECKOFFS AND CHECK YOURSELFS
    checkoffs = [0]
    def docheckoff(match):
        d = match.groupdict()
        checkoffs[0] += 1
        return '<div class="checkoff"><h4 class="checktext">Checkoff %d:</h4><p>%s</p><p><span id="queue_checkoff_%d"></span></p></div>' % (checkoffs[0], d['body'], checkoffs[0])
    text=re.sub(environment_matcher('checkoff'), docheckoff, text)

    checkyourself = [0]
    def docheckyourself(match):
        d = match.groupdict()
        checkyourself[0] += 1
        return '<div class="question"><b>Try Now:</b><p>%s</p><p><span id="queue_checkyourself_%d"></span></p></div>' % (d['body'], checkyourself[0])
    text=re.sub(environment_matcher('checkyourself'), docheckyourself, text)

    # TUTORONLY and PDFONLY
    text = re.sub(environment_matcher('tutoronly'), lambda m: m.groupdict()['body'], text)
    text = re.sub(environment_matcher('pdfonly'), '', text)

    # GOALS
    text = re.sub(environment_matcher('goals'), lambda m: '<div class="question"><h2 class="goalh2">Goals:</h2>%s</div>' % m.groupdict()['body'], text)

    # CRITICAL
    text = re.sub(environment_matcher('critical'), lambda m: '<div class="critical">%s</div>' % m.groupdict()['body'], text)
    # NOTES:
    text = re.sub(environment_matcher('note'), lambda m: '<div class="note">%s</div>' % m.groupdict()['body'], text)

    #TYPES OF CODE
    #c/c++
    text = re.sub(environment_matcher('codec'), lambda m: '<code class="prettyprint lang-cpp">%s</code>' % m.groupdict()['body'], text)
    #python:
    text = re.sub(environment_matcher('codep'), lambda m: '<code class="prettyprint lang-python">%s</code>' % m.groupdict()['body'], text)
    #c/c++
    text = re.sub(environment_matcher('prec'), lambda m: '<pre class="prettyprint linenums lang-cpp">%s</pre>' % m.groupdict()['body'], text)
    #python:
    text = re.sub(environment_matcher('prep'), lambda m: '<pre class="prettyprint linenums lang-python">%s</pre>' % m.groupdict()['body'], text)

    # ANSWERS, LAB INFO, ETC
    for tag in ('answers','notanswers','labnum','labtype'):
        text=re.sub(environment_matcher(tag), lambda m: '', text)

    def titlematcher(m):
        global labtitle
        labtitle=m.groupdict().get('body','')
        return ''
    text = re.sub(environment_matcher('labtitle'), titlematcher, text)

    # PAGE BREAKS
    text = re.sub('<page(.*?)>', '<div class="pagebreak"></div>', text)

    # FRAMED TEXT
    text = re.sub(environment_matcher('framedtext'), lambda x:'<div class="question">%s</div>' % x.groups()[0], text)


    return text












# EXTENSIONS FOR 6.002

import cmath

def _draw_exp(args):
    o = r"\text{exp}(%s)" % ','.join(args)
    if len(args) != 1:
        return o, r"$\text{exp}$ should take exactly one argument."
    return o

csq_funcs = {
    'exp': (cmath.exp, _draw_exp)
}


def is_near(c):
    def closer(sub,soln):
        if soln==0:
            return abs(sub)<c
        else:
            return (abs(sub-soln) /abs(soln)) <= c
    return closer 

# PYTHON SANDBOX

csq_python_sandbox = "python"
if '608' in cs_url_root:
    csq_python_interpreter = '/home/catsoop/python3sandbox/bin/python3'
    cs_checker_websocket = 'wss://iesc-s2.mit.edu/reporter2'
else:
    csq_python_interpreter = '/usr/bin/python3'
    cs_checker_websocket = 'ws://localhost:6011'
csq_python3 = True
csq_sandbox_options = {'MEMORY': 1e9}
csq_syntax = 'python'


# PERMISSIONS

cs_default_role = 'Guest'
cs_permissions = {'Admin': ['view_all', 'submit_all', 'impersonate', 'admin', 'staff', 'whdw', 'email', 'checkoff'],
               'Instructor': ['view_all', 'submit_all', 'impersonate', 'admin', 'staff', 'whdw', 'email', 'checkoff'],
               'TA': ['view_all', 'submit_all', 'impersonate','staff', 'whdw', 'email', 'admin', 'checkoff'],
               'UTA': ['view_all', 'submit_all', 'impersonate', 'staff', 'whdw', 'admin', 'checkoff'],
               'LA': ['view_all', 'submit_all','staff', 'checkoff'],
               'Student': ['view', 'submit'],
               'SLA': ['view', 'submit', 'staff', 'checkoff'],
               'Guest': ['view']}

#Scheduling
cs_first_monday = '2018-02-05:00:00' #necessary for relative times to work
require_section = True
sections = {1:'TR-AM', 2:'TR-MID', 3:'TR-PM'}
section_times = {'default': {'wks':'M:15:00', 'wke':'U:23:59', 'las':'R:19:00', 'lae':'R:21:55', 'lbs':'T:19:05', 'lbe':'T:20:25', 'staffmtg':'M:16:00'},
                 1: {'las':'T:09:00', 'lae':'T:11:30', 'lbs':'R:09:00', 'lbe':'R:11:30'},
                 2: {'las':'T:12:00', 'lae':'T:14:30', 'lbs':'R:12:00', 'lbe':'R:14:30'},
                 3: {'las':'T:14:30', 'lae':'T:17:00', 'lbs':'R:14:30', 'lbe':'R:17:00'},
                 'STAFF': {'las':'M:11:00', 'lae': 'T:19:00', 'lbs':'M:13:00', 'lbe': 'M:19:00',},
                }
cs_sections = list(sections.keys())

def cs_realize_time(meta, rel):
    uinfo = meta.get('cs_user_info', {})
    section = uinfo.get('section',None)
    #if section is None:
    #    return csm_time.realize_time(meta, 'NEVER')
    role = uinfo.get('role',None)
    #if section is None:
    #    return csm_time.realize_time(meta, 'NEVER')
    default = section_times.get('default',{})
    special = section_times.get(section,{})
    wknum = 0
    for (k,v) in list(special.items()) + list(default.items()):
        if rel.startswith(k):
            wknum = int(rel.split(':')[1])
            if wknum >=8:
                wknum +=1
            meta['cs_week_number'] = wknum
            
            rel = v
            break
    return csm_time.realize_time(meta,rel)

cs_checker_global_timeout = 180

def cs_post_load(context):
    if 'cs_long_name' in context:
        context['cs_content_header'] = context['cs_long_name']
    x = context['cs_path_info'][-1]
    labtype=None
    r = context.get('cs_user_info', {}).get('role',None)
    if x.endswith('a'):
        labtype = 'Lab'
        labnum = x[-3:]
    elif x.endswith('b'):
        labtype = 'Lab'
        labnum = x[-3:]
    if labtype is not None:
        context['cs_content_header'] = '%s %s%s' % (labtype,labnum,(': '+context['labtitle'].replace('\\crlf', '<br/>')) if 'labtitle' in context else '')
    is_dl = labtype == 'Lab'
    is_handout =x.endswith('.zip') or x.endswith('.pdf')
    is_staff = r in ('SLA', 'LA') or context.get('cs_user_info', {}).get('username', None) in ('adat',)
    if is_staff:
        if is_dl or is_handout:
            context['cs_user_info']['section'] = 'STAFF'
    try:
        loc = os.path.abspath(os.path.join(context['cs_data_root'], 'courses', *context['cs_path_info']))
        git_info = subprocess.check_output(["git", "log", "--pretty=format:%h %ct",
                                            "-n1", "--", "content.md", "content.xml",
                                            "content.py"], cwd=loc)
        h, t = git_info.split()
        t = context['csm_time'].long_timestamp(datetime.fromtimestamp(float(t))).replace(';', ' at')
        context['cs_footer'] = 'This page was last updated on %s (revision <code>%s</code>).<br/>&nbsp;<br/>' % (t, h.decode())
    except:
        pass

csq_receiver = 'https://visor.mit.edu/coderunner_receiver'
csq_websocket = 'wss://visor.mit.edu/coderunner_status'

def cs_due_date_message(duedate):
    return '<center>This assignment is due on %s.<br/><hr/><br/></center>' % duedate.replace(';', ' at')

def get_dex_status(graded):
    if graded:
        return "GRADED: See page for score"
    else:
        return "Not Graded Yet"

# DO EXERCISES
def get_icon(activity):
    if str(cs_username) == 'None':
        return ''
    due_date = cs_due_date 
    stats = csm_tutor.compute_page_stats(globals(), cs_username, cs_path_info+[activity], ['question_info', 'state', 'context'])
    log = stats['state']
    aq = [i for i in stats['question_info'].keys() if stats['context']['cs_defaulthandler_name_map'][i][0]['qtype'] != 'checkyourself']
    onesubs = [i for i in aq if log.get('nsubmits_used',{}).get(i,None) == 1]
    onesubbed = all(i in onesubs for i in aq)
    submitted = log.get('last_submit_time',None)
    due = cs_realize_time(globals(), due_date)
    #take extensions into account...
    e = cs_user_info.get('extensions',[])
    for i in e:
        if re.match(i[0][0],'.'.join(cs_path_info[1:]+[activity])):
            due += csm_time.timedelta(weeks=i[0][1])
    so = cs_user_info.get('score_override',[])
    for i in so:
        if re.match(i[0],'.'.join(cs_path_info[1:]+[activity])):
            score = i[1]
    perfect = True
    for i in aq:
        temp = log.get('scores', {}).get(i, 0.0)
        if temp == None:
            perfect = False
            break
        elif abs(log.get('scores', {}).get(i, 0.0) -1.0) >= 1e-5:
            perfect = False
            break
    if submitted is not None:
        if not perfect:
            return '<img class="progressimage" src="COURSE/images/warning.png"/>'
        else:
            if csm_time.from_detailed_timestamp(submitted) > due:
                return '<img class="progressimage" src="COURSE/images/complete_but_late.png" />'
            else:
                if onesubbed:
                    return '<img class="progressimage" src="COURSE/images/perfect.png" /><img class="progressimage" src="COURSE/images/one_submit.png" />'
                else:
                    return '<img class="progressimage" src="COURSE/images/perfect.png" />'
    return '<img src="COURSE/images/attention.png" class="progressimage" title="Not attempted / submitted"/>'


# * <img class="progressimage" src="COURSE/images/attention.png" />: Not attempted / submitted
# * <img class="progressimage" src="COURSE/images/warning.png"/>: Attempted but not complete
# * <img class="progressimage" src="COURSE/images/complete_but_late.png" />: Complete but late
# * <img class="progressimage" src="COURSE/images/perfect.png" />: Complete and on time
# * <img class="progressimage" src="COURSE/images/perfect.png" /><img class="progressimage" src="COURSE/images/one_submit.png" />: Complete and on time, using only one submission per question



def do_exercise(name,optional=False, done=False):
    if name in cs_children:
        info = cs_children[name]
        due_date = tutor.get_due_date(info)
        long_name = ': '+info['cs_long_name']
        if optional:
            return '<li><a href="CURRENT/%s">Exercise%s</a> %s <i>(optional)</i></li>' % (name, long_name, get_dex_status(done))
        else:
            return '<li><a href="CURRENT/%s">Exercise%s</a> %s (Due %s)</li>' % (name, long_name, get_icon(name), csm_time.short_timestamp(due_date))
    else:
        return '<li><b><font color="red">No such exercise: %s</font></b></li>' % name

def do_exercises(ex=None,optional=False, done=False):
    cs_print('<ul>'+'\n'.join(do_exercise(i,optional,done) for i in (cs_children if ex is None else ex))+'\n</ul>')



cs_scripts = """
<style>
blockquote {
    background-color: #f5f5f5;
    border-color: #dddddd !important;
    font-size: 85%;
}
img.progressimage {
   height:2em;
   width:2em;
}
</style>
"""

GRADING_KEY = '''
<p>&nbsp;</p>
<hr/>

**Symbol Key**:

* <img class="progressimage" src="COURSE/images/attention.png" />: Not attempted / submitted
* <img class="progressimage" src="COURSE/images/warning.png"/>: Attempted but not complete
* <img class="progressimage" src="COURSE/images/complete_but_late.png" />: Complete but late
* <img class="progressimage" src="COURSE/images/perfect.png" />: Complete and on time
* <img class="progressimage" src="COURSE/images/perfect.png" /><img class="progressimage" src="COURSE/images/one_submit.png" />: Complete and on time, using only one submission per question

<p>&nbsp;</p>
<center>
<small>
Note: the images used to indicate progress are either exact copies (smiley, really happy smiley) or slightly modified versions (warning sign, thinking, really happy smiley with sunglasses) of emoji graphics by <a href="http://emojione.com" target="_blank">EmojiOne</a>.<br/>These images are available under a <a href="http://creativecommons.org/licenses/by/4.0/" target="_blank">Creative Commons Attribution 4.0 International</a> license.
</small>
'''

from collections import defaultdict

def cs_pre_handle(context):
    textsections = [None, 0, 0, 0]
    tags = [
        'chapter',
        'section',
        'subsection',
        'subsubsection',
    ]

    counts = {
        'checkoff': 0,
        'checkyourself': 0,
        None: 0,
    }
    texts = defaultdict(lambda: 'Tutor Question {count} in Section {section}', {
            'checkoff': 'Checkoff {count}',
            'checkyourself': 'Check Yourself {count}',
    })

    for problem in context.get('cs_problem_spec', []):
        if type(problem) == str:
            section_re = re.compile(r'''
            <
            \s*
            (?P<name>chapter|(sub){0,2}section)
            .*?
            (num\s*(?P<quote>['"])=\s*(?P<num>\d+)(?P=quote))?
            \s*
            >
            ''', re.VERBOSE)
            for match in section_re.finditer(problem):
                name = match.group('name')
                index = tags.index(name)

                if match.group('num') is not None:
                    num = int(match.group('num') or '0')
                    textsections[index] = num
                else:
                    if textsections[index] is None:
                        textsections[index] = 0
                    textsections[index] += 1

                textsections[index+1:] = [0]*(len(textsections) - (index + 1))
                # checkoff and checkyourself are counted per-page,
                # but everything else is per-section
                counts = {
                    'checkoff': counts['checkoff'],
                    'checkyourself': counts['checkyourself'],
                    None: 0,
                }
        else:
            qtype, qinfo = problem

            if qtype['qtype'] in counts:
                counts[qtype['qtype']] += 1
                count = counts[qtype['qtype']]
            else:
                counts[None] += 1
                count = counts[None]

            text = texts[qtype['qtype']]

            if 'csq_display_name' not in qinfo:
                qinfo['csq_display_name'] = text.format(
                    count = count,
                    section = '.'.join(str(n) for n in textsections if n),
                )
            else:
                if qtype['qtype'] == 'checkyourself':
                    qinfo['csq_display_name'] = 'Check Yourself {}: {}'.format(
                        counts[qtype['qtype']],
                        qinfo['csq_display_name'],
                    )
            qinfo['csq_display_count'] = count

if any(part.startswith('lab') for part in cs_path_info):
    queue_enable = True
if any(part.startswith('EX') for part in cs_path_info):
    cs_whdw_no_section = True

queue_room_name = '38-530'
queue_room = '38-530'

