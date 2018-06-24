

defaults = {'csq_soln':(), 
            'csq_check_resolution': 0.01,
            'csq_npoints':1, 
            'csq_msg_function':lambda sub: (''), 
            'csq_show_check':False,
            'csq_prompt':'',
            'csq_box_prompt' : ['']}

def strip_zeros(l):
    while len(l) > 0 and l[-1] == 0:
        l.pop()

def check_equivalent(a,b):
    return all(abs(x-y)<1e-6 for x,y in zip(a,b)) and len(a)==len(b)


def escape(s):
    return s.replace('"','&quot;')

def total_points(**kwargs):
    info = dict(defaults)
    info.update(kwargs)
    return info['csq_npoints']

def handle_submission(submissions, **kwargs):
    info = dict(defaults)
    info.update(kwargs)

    def is_close(x,y):
        if x==0 or y ==0:
            return abs(x-y)<info['csq_check_resolution']
        else:
            return abs(x-y)/abs(y)<info['csq_check_resolution']

    def default_check_function(sub,sol):
        ok_list = []
        score =0
        per = 1.0/len(sol)
        if len(sub)!=len(sol):
            return 0.0,["Incorrect" for x in range(len(sol))]
        for i in range(len(sol)):
            if is_close(sub[i],sol[i]):
                ok_list.append('''<font color="#32CD32">Correct</font>''')
                score+=per
            else:
                ok_list.append('''<font color="red">Incorrect</font>''')
        return score,ok_list
    defaultstr = '('
    for x in range(len(info['csq_soln'])):
        defaultstr +='"",'
    defaultstr+=')'
    try:
        start = submissions.get('%s' % info['csq_name'],defaultstr)
        start = eval(start)
        start = [float(x) for x in start]
        percent,good = default_check_function(start,info['csq_soln'])
        broke = False
    except:
        percent = 0.0
        good = False
        broke = True
    if info['csq_show_check']:
        if percent == 1.0:
            msg = '<img src="BASE/images/check.png" />'
        elif percent == 0.0:
            msg = '<img src="BASE/images/cross.png" />'
        else:
            msg = ''
    else:
        msg = ''
    if broke:
        msg += '<p><div class="response" id="%s_response">Please a valid answer in each box.</div>' % (info['csq_name'])
    else:
        msg += '<p><div class="response" id="%s_response">'%(info['csq_name'])
        for x in range(len(info['csq_box_prompt'])):
            msg+='<p>%s: %s</p>' %(info['csq_box_prompt'][x],good[x])
        msg+= ' </div>' 
    msg += '''<script type="text/javascript">MathJax.Hub.Queue(["Typeset",MathJax.Hub,"%s_response"]);</script>''' % info['csq_name']
    return {'score': percent, 'msg': msg}

def render_html(last_log, **kwargs):
    info = dict(defaults)
    info.update(kwargs)
    defaultstr = '('
    for x in range(len(info['csq_soln'])):
        defaultstr +='"",'
    defaultstr+=')'
    if last_log is None:
        last_log = {}
    length = len(info['csq_soln'])
    sub = eval(last_log.get(info['csq_name'],defaultstr))
    name = info['csq_name']
    out = ""
    for xx in range(length):
        out += '<p>%s: <input type="text"' %(info['csq_box_prompt'][xx])
        if info.get('csq_size',None) is not None:
            out += ' size="%s"' %(info['csq_size'])
        out += ' value="%s"' %(sub[xx])
        out += ' name="%s_%d"' %(info['csq_name'],xx)
        out += ' id="%s_%d"' %(info['csq_name'],xx)
        out += ' class="%s_group"'%(info['csq_name'])
        out += ' /></p>'
    out += '\n<input type="hidden" value="%s" name="%s" id="%s"/>' % (escape(repr(sub)), info['csq_name'],info['csq_name'])
    out += '''\n<script type="text/javascript">function do_%s_update(e){\n'''%(info['csq_name'])
    out += '''var answers_%s =[];\n'''%(info['csq_name'])
    for xx in range(length):
        out+='''answers_%s.push($('#%s_%d').val());\nconsole.log($('#%s_%d').val());\n'''%(info['csq_name'],info['csq_name'],xx,info['csq_name'],xx)
    out+='''$("#%s").val(JSON.stringify(answers_%s));'''%(info['csq_name'],info['csq_name'])
    out+='''$("#%(name)s_check").trigger("click");
        console.log(answers_%(name)s);
        }
        do_%(name)s_update(null);
        $(".%(name)s_group").keyup(do_%(name)s_update);
        </script>''' % {'name':info['csq_name']}
    return out

def answer_display(**kwargs):
    info = dict(defaults)
    info.update(kwargs)
    out= "<p>Solution:<p>"
    length = len(info['csq_soln'])
    for xx in range(length):
        out+="<p>%s: %f</p>"%(info['csq_box_prompt'][xx],info['csq_soln'][xx])
    return out
