import os
response = ""
grade_fname = os.path.join(cs_data_root, 'courses', cs_course, 'progress', '_grades.py')

with open(grade_fname) as f:
    exec(f.read())

ex_weight = 20 * 1/len(exercises)
lab_weight = 10 * 1/len(labs)

theweek = cs_form.get('week', None)

a6e = {1:[['cbasics','pretty_print','dt_physics'],[1,4,3],'Exercise 01'],
2: [['pointers','sm1','physics_sim','angle','power1'],[2,4,7,1,3],'Exercise 02'],
3: [['pointersandfunctions','filters','ribosome','server_side','power2'],[3,5,5,2,4],'Exercise 03'],
4: [['lpfilter','power3','button','httpget','wikipedia_be'],[2,4,6,1,4],'Exercise 04'],
5: [['game_time','competitor','wikipedia_fe','voltage_division'],[2,3,5,2],'Exercise 05'],
6: [['xcorr_1','resampling','gesture_recognition','data_life'],[3,3,1,3],'Exercise 06'],
7: [['caesar_vigenere_1','caesar_vigenere_2','cracking','power4','c_libraries','python_libraries'],[3,3,4,3,1,1],'Exercise 07'],
8: [['key_exchange'],[1],'Exercise 08'],
}


def extensions_for_week(wk):
    out = []
    #no extensions for these weeks yet
    for d in range(len(a6e[wk][0])):
        out.append((['ex%02d' % (wk),a6e[wk][0][d]], 20*1.0/8*a6e[wk][1][d]/sum(a6e[wk][1])))
    if wk==1:
        out.append((['lab01a'],15*1.0/12))
        out.append((['lab01b'],15*1.0/12))
    elif wk==2:
        out.append((['lab02a'],15*1.0/12))
        out.append((['lab02b'],15*1.0/12))
    elif wk==3:
        out.append((['lab03b'],15*1.0/12))
    elif wk==4:
        out.append((['lab04a'],15*1.0/12))
        out.append((['lab04b'],15*1.0/12))
    elif wk==5:
        out.append((['lab05a'],15*1.0/12))
        out.append((['lab05b'],15*1.0/12))
    elif wk==6:
        out.append((['lab06a'],15*1.0/12))
    elif wk==7:
        out.append((['lab07b'],15*1.0/12))
    else:
        out.append((['lab08a'],15*1.0/12))
    #out.append(('lab%02da' %wk,15*1.0/15))
    #out.append(('lab%02db' %wk,15*1.0/15))
    return out

def hw_lab_ex_points(wk, autoext):
    ptsback = 0
    for path, weight in extensions_for_week(wk):
        back = total_lateness(path, [int(i) for i in autoext]) * weight
        cs_debug(str(path),str([int(i) for i in autoext]),str(back))
        ptsback += back
    cs_debug(ptsback)
    return ptsback


if theweek is not None:
    s1 = hw_lab_ex_points(int(theweek), [int(theweek)])
    s2 = hw_lab_ex_points(int(theweek), [int(theweek), int(theweek)])
else:
    s1 = s2 = 0

cs_handler = 'raw_response'
content_type = 'text/plain'
response = '%s\n%s' % (s1, s2)
