defaults = {'csq_soln':([],[]), 
            'csq_check_function':lambda sub,soln: (sub.strip()==soln.strip()),
            'csq_npoints':1, 
            'csq_msg_function':lambda sub: (''), 
            'csq_show_check':False,
            'csq_diffeq_terms':['y','x'],
            'csq_prompt':''}

def str2(n):
    return str(n)

def d_text(d,term):
    out = ""
    if len(d) > 0:
        out += ("%s %s[n]" % (str2(d[0]) if d[0] != 1 else "",term)) if d[0] != 0 else ""
    if len(d) > 1:
        if len(out) > 0:
            out += " + "
        out += " + ".join(["%s %s[n-%d]" % (str2(d[i]) if d[i] != 1 else "",term,i) for i in range(1,len(d)) if d[i] != 0])
    return out
                                                                        
def c_text(c,term):
    return " + ".join(["%s %s[n-%d]" % (str2(c[i]) if c[i] != 1 else "",term,i+1) for i in range(len(c)) if c[i] != 0])

def strip_zeros(l):
    while len(l) > 0 and l[-1] == 0:
        l.pop()

def check_equivalent(a,b):
    return all(abs(x-y)<1e-6 for x,y in zip(a,b)) and len(a)==len(b)

def check_diffeq(act,sub):
    #def check_diffeq((c,d),(cs,ds)):
    strip_zeros(act[0])
    strip_zeros(act[1])
    return check_equivalent(act[0],sub[0]) and check_equivalent(act[1],sub[1])

def to_diffeq(a,terms):
    c,d = a
    from_d = d_text(d,terms[1])
    from_c = c_text(c,terms[0])
    out = r'''{}[n] = '''.format(terms[0])
    out += from_d
    if len(from_d) > 0 and len(from_c) > 0:
        out += " + "
    out += from_c
    return out

def escape(s):
    return s.replace('"','&quot;')

def total_points(**kwargs):
    info = dict(defaults)
    info.update(kwargs)
    return info['csq_npoints']

#checktext = "Check Syntax"
#def handle_check(submissions, **kwargs):
#    info = dict(defaults)
#    info.update(kwargs)
#    try:
#        sub = eval(submissions.get('%s' % info['csq_name'],'("","")'))
#        d = eval(sub[0])
#        c = eval(sub[1])
#        assert (isinstance(c,list) and isinstance(d,list))
#        broke = False
#    except:
#        percent = 0.0
#        broke = True
#    msg = ''
#    if broke:
#        msg += '<p><div class="response" id="%s_response">Please enter a valid Python list in each box.</div>' % info['csq_name']
#    else:
#        msg += '<p><div class="response" id="%s_response">The coefficients you submitted/saved represent the following difference equation:<p>\[%s\]</div>' % (info['csq_name'],to_diffeq((c,d)))
#    msg += '''<script type="text/javascript">MathJax.Hub.Queue(["Typeset",MathJax.Hub,"%s_response"]);</script>''' % info['csq_name']
#    return msg

def handle_submission(submissions, **kwargs):
    info = dict(defaults)
    info.update(kwargs)
    try:
        sub = eval(submissions.get('%s' % info['csq_name'],'("","")'))
        d = eval(sub[0])
        c = eval(sub[1])
        assert (isinstance(c,list) and isinstance(d,list))
        percent = check_diffeq((c,d),info['csq_soln'])
        broke = False
    except:
        percent = 0.0
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
        msg = ''
        #msg += '<p><div class="response" id="%s_response">Please enter a valid Python list in each box.</div>' % info['csq_name']
    else:
        msg=''
        #msg += '<p><div class="response" id="%s_response">The coefficients you entered represent the following difference equation:<p>\[%s\]</div>' % (info['csq_name'],to_diffeq((c,d)))
    msg += '''<script type="text/javascript">MathJax.Hub.Queue(["Typeset",MathJax.Hub,"%s_response"]);</script>''' % info['csq_name']
    return {'score': percent, 'msg': msg}

def render_html(last_log, **kwargs):
    info = dict(defaults)
    info.update(kwargs)
    
    if last_log is None:
        last_log = {}
    sub = eval(last_log.get(info['csq_name'],'("","")'))
    d = sub[0]
    c = sub[1]

    name = info['csq_name']
    out = ''
    out += info['csq_prompt']
    out += '<p><b>Difference Equation:</b></p><center>dCoeffs (input): <input type="text"'
    if info.get('csq_size',None) is not None:
        out += ' size="%s"' % info['csq_size']

    out += r' value="%s"' % escape(d)
    out += r' name="%s_1"' % info['csq_name']
    out += r' id="%s_1"' % info['csq_name']
    out += r' /><br/>'
    out += r'cCoeffs (output): <input type="text"'
    if info.get('size',None) is not None:
        out += r' size="%s"' % info['csq_size']
    out += r' value="%s"' % escape(c)
    out += r' name="%s_2"' % info['csq_name']
    out += r' id="%s_2"' % info['csq_name']
    out +=r' /><br/></center>'
    out += '''<span class="eq_display_area" style="display:block;"><center><p id="error_indication_{0}" style="color:red;"></p><p>The coefficients currently entered represent the following difference equation:</p><p id="displayed_eq_{0}">$$y[n] = 0$$</p></center></span>'''.format(info['csq_name'])
    out += '\n<input type="hidden" value="%s" name="%s" id="%s" />' % (escape(repr(sub)), info['csq_name'], info['csq_name'])
    out += '''<script type="text/javascript">function do_%(name)s_update(e){
        var d = $('#%(name)s_1').val();
        var c = $('#%(name)s_2').val();
        $("#%(name)s").val(JSON.stringify([d,c]));
        $//("#%(name)s_check").trigger("click");
        }
        do_%(name)s_update(null);
        $("#%(name)s_1").keyup(do_%(name)s_update);
        $("#%(name)s_2").keyup(do_%(name)s_update);
        var coeffs_%(name)s = {x0:0,x1:0,x2:0,x3:0,x4:0,x5:0,x6:0,x7:0,x8:0,x9:0,x10:0,y1:0,y2:0,y3:0,y4:0,y5:0,y6:0,y7:0,y8:0,y9:0,y10:0};
        var names_%(name)s = {y10:"%(y)s[n-10]",y9:"%(y)s[n-9]", y8:"%(y)s[n-8]",y7: "%(y)s[n-7]",y6:"%(y)s[n-6]",y5:"%(y)s[n-5]",y4:"%(y)s[n-4]",y3:"%(y)s[n-3]",y2:"%(y)s[n-2]",y1:"%(y)s[n-1]",x10:"%(x)s[n-10]",x9:"%(x)s[n-9]",x8:"%(x)s[n-8]",x7: "%(x)s[n-7]",x6:"%(x)s[n-6]",x5:"%(x)s[n-5]",x4:"%(x)s[n-4]",x3:"%(x)s[n-3]",x2:"%(x)s[n-2]",x1:"%(x)s[n-1]",x0:"%(x)s[n]"};

    function render_display_string_%(name)s() {
          $("#error_indication_%(name)s").text("");
          var error_str = " ";
          var display_string = "%(y)s[n]=";
          var first_value = true;
          var y_raw = $('#%(name)s_2').val().replace(" ","");
          var x_raw = $('#%(name)s_1').val().replace(" ","");
          if (y_raw.charAt(0)!="[" || y_raw.charAt(y_raw.length -1) != "]"){
            error_str += "C coefficients not Python list. ";
          } else{
            var y_coeffs = y_raw.replace("[","").replace("]","").split(",");
            for (var co=10; co>=0;co--){
              if(co<y_coeffs.length){
                var candidate  = parseFloat(y_coeffs[co]);
                if (isNaN(candidate) && y_coeffs.length!= 1){
                  error_str += "Unknown Characters in C coefficients! ";
                  candidate = 0;
                }
                coeffs_%(name)s["y"+String(co+1)]=candidate;
              }else{
                coeffs_%(name)s["y"+String(co+1)]=0;
              }
            }
          }
          if (x_raw.charAt(0)!="[" || x_raw.charAt(x_raw.length -1) != "]"){
            error_str += "D coefficients not Python list. ";
          } else{
            var x_coeffs = x_raw.replace("[","").replace("]","").split(",");
            for (var co=11; co>=0;co--){
              if(co<x_coeffs.length){
                var candidate  = parseFloat(x_coeffs[co]);
                if (isNaN(candidate) && x_coeffs.length!= 1){
                    console.log(candidate);
                    error_str += "Unknown Characters in D coefficients!";
                    candidate = 0;
                }
                coeffs_%(name)s["x"+String(co)]=candidate;
              }else{
                coeffs_%(name)s["x"+String(co)]=0;
              }
            }
          }
          for (var co in coeffs_%(name)s){
            //console.log(coeffs_%(name)s[co]);
            if (coeffs_%(name)s[co]>0){
              if (first_value){
                if (coeffs_%(name)s[co]==1) {
                  display_string +=names_%(name)s[co]; 
                } else {
                  display_string += coeffs_%(name)s[co] + names_%(name)s[co];
                }  
                first_value = false;
              }else{
                if (coeffs_%(name)s[co]==1) {
                  display_string += "+"+names_%(name)s[co]; 
                } else {
                  display_string += "+" +coeffs_%(name)s[co] + names_%(name)s[co];
                } 
              }
            }else if (coeffs_%(name)s[co]<0){
              if (first_value){
                first_value = false;
              }
              if (coeffs_%(name)s[co]==-1) {
                display_string += "-" + names_%(name)s[co];
              } else {
                display_string += coeffs_%(name)s[co]+names_%(name)s[co];
              }
            }   
          }
          if (error_str != " "){
            error_str = "ERROR: " + error_str;
            display_string = "";
          }
          $("#error_indication_%(name)s").text(error_str);
          $("#displayed_eq_%(name)s").html("<span class='cs_math_to_render'>"+display_string+"</span>");
          console.log(display_string);
          //MathJax.Hub.Queue(["Typeset",MathJax.Hub,'#displayed_eq_%(name)s']);
          catsoop.render_math($("#displayed_eq_%(name)s"), true);
    }

    $("#%(name)s_2").keyup(function(){
      render_display_string_%(name)s();
    });
    $("#%(name)s_1").keyup(function(){
      render_display_string_%(name)s();
    });
    render_display_string_%(name)s();


        </script>''' % {'name':info['csq_name'],'y':info['csq_diffeq_terms'][0].replace('\\','\\\\'),'x':info['csq_diffeq_terms'][1].replace('\\','\\\\')}
    return out

def answer_display(**kwargs):
    info = dict(defaults)
    info.update(kwargs)
    #print(info['csq_soln'][::-1])
    #out = "{}".format(info['csq_soln'][::-1])
    c = info['csq_soln'][::-1]
    out= "<p>Solution:<p>dCoeffs (input): <tt>{0}</tt><p>cCoeffs (output): <tt>{1}</tt><p><span id='{2}_soln'>\[{3}\]</span>".format(c[0],c[1],info['csq_name'],to_diffeq(info['csq_soln'],info['csq_diffeq_terms']))
    out += '''<script type="text/javascript">MathJax.Hub.Queue(["Typeset",MathJax.Hub,"%s_soln"]);</script>''' % info['csq_name']
    return out
