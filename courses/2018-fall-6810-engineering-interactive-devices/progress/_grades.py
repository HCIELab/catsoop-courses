import json
import builtins
from collections import OrderedDict
from datetime import timedelta

# this was here to automatically grab assignments.  but now they're pre-populated...
#labs = sorted(csm_loader.get_subdirs(globals(), cs_course, ['labs']))
#homeworks = sorted(csm_loader.get_subdirs(globals(), cs_course, ['homework']))
#exercises = sorted(csm_loader.get_subdirs(globals(), cs_course, ['exercises']))
#nqs = sorted(csm_loader.get_subdirs(globals(), cs_course, ['nqs']))


# FILL THESE IN WITH ASSIGNMENTS THAT HAVE BEEN RELEASED
labs = ['lab01a', 'lab01b','lab02a','lab02b','lab03b','lab04a','lab04b','lab05a','lab05b','lab06a','lab07b','lab08a']
exercises = ['ex01', 'ex02', 'ex03', 'ex04','ex05','ex06','ex07','ex08']

all_608_exes = {'ex01':[['cbasics','pretty_print','dt_physics'],[1,4,3],'Exercise 01'],
'ex02': [['pointers','sm1','physics_sim','angle','power1'],[2,4,7,1,3],'Exercise 02'],
'ex03': [['pointersandfunctions','filters','ribosome','server_side','power2'],[3,5,5,2,4],'Exercise 03'],
'ex04': [['lpfilter','power3','button','httpget','wikipedia_be'],[2,4,6,1,4],'Exercise 04'],
'ex05': [['game_time','competitor','wikipedia_fe','voltage_division'],[2,3,5,2],'Exercise 05'],
'ex06': [['xcorr_1','resampling','gesture_recognition','data_life'],[3,3,1,3],'Exercise 06'],
'ex07': [['caesar_vigenere_1','caesar_vigenere_2','cracking','power4','c_libraries','python_libraries'],[3,3,4,3,1,1],'Exercise 07'],
'ex08': [['key_exchange'],[1],'Exercise 08'],
}


spbk_start = datetime(2018,3,25,23,59)
spbk_end = datetime(2018,3,30,23,59)
FOURTEENDAYS = 14*24*60*60


def late_penalty(qinfo, sub, due):
    if due < spbk_start:
        if sub > spbk_end:
            sub -= (spbk_end-spbk_start)
        elif sub > spbk_start:
            sub = spbk_start 
    if qinfo['qtype'] == 'checkoff':
        return checkoff_late_penalty(sub, due)
    else:
        return regular_late_penalty((sub-due).total_seconds())

def regular_late_penalty(seconds_late):
    return max(0, min(1, 1 - seconds_late/FOURTEENDAYS))

# maps DOW (Monday = 0) to start and end times of office hours on that day, for
# use with checkoff lateness penalty
_officehours = {
    1: (19, 21),
    2: (19, 22),
    4: (12, 16),
    6: (16, 20),
}

def checkoff_late_penalty(sub, due):
    t = 0
    while due <= sub:
        h = _officehours.get(sub.weekday(), (0,0))
        if due.date() == sub.date():
            if h == (0,0) or sub.hour < h[0]:
                pass
            elif sub.hour < h[1]:
                t += ((sub.hour - h[0])*60. + due.minute) * 60
            else:
                t += (h[1]-h[0])*60.*60
            break
        else:
            t += (h[1]-h[0])*60.*60
        sub -= csm_time.timedelta(days=1)
    return regular_late_penalty(t)


'''
        if wk == 7:
            out.append((['homework', 'hw%02d' % wk], 7))
        elif wk == 8:
            out.append((['homework', 'hw%02d' % wk], 7))
            out.append((['exercises', 'ex%02d' % wk], 7))
            out.append((['labs', 'lab%02d' % (wk-1)], 7))
        else:
            out.append((['exercises', 'ex%02d' % (wk+1)], 7))
            out.append((['labs', 'lab%02d' % wk], 7))
'''

exset = {1:['cbasics','pretty_print','dt_physics'],
2: ['pointers','sm1','physics_sim','angle','power1'],
3: ['pointersandfunctions','filters','ribosome','server_side','power2'],
4: ['lpfilter','power3','button','httpget','wikipedia_be'],
5: ['game_time','competitor','wikipedia_fe','voltage_division'],
6: ['xcorr_1','resampling','gesture_recognition','data_life'],
7: ['caesar_vigenere_1','caesar_vigenere_2','cracking','power4','c_libraries','python_libraries'],
8: ['key_exchange'],
}

def extensions_from_weeks(weeks):
    out = []
    #return out
    for wk in weeks:
        for d in exset[wk]:
            out.append((['ex%02d' % (wk),d], 7))
        if wk == 1:
            out.append((['lab01a'],7))
            out.append((['lab01b'],7))
        if wk == 2:
            out.append((['lab02a'],7))
            out.append((['lab02b'],7))
        if wk == 3:
            out.append((['lab03b'],7))
        if wk == 4:
            out.append((['lab04a'],7))
            out.append((['lab04b'],7))
        if wk == 5:
            out.append((['lab05a'],7))
            out.append((['lab05b'],7))
        if wk == 6:
            out.append((['lab06a'],7))
        if wk == 7:
            out.append((['lab07b'],7))
        if wk == 8:
            out.append((['lab08a'],7))
    return out


def get_extension(path, name, cache, auto_ext=None):  # number of seconds this has been extended by
    if auto_ext is None:
        auto_ext = []
    ext = 0
    #cs_debug(path)
    #cs_debug("GET Extension: ",str(auto_ext))
    for e in cs_user_info.get('extensions', []) + extensions_from_weeks(auto_ext):
        if all(i==j for i,j in zip(e[0], path + [name])):
            #cs_debug(e[0])
            #cs_debug(path+[name])
            ext += e[1]*24*60*60
    if ext:
        cache[name] = True
    return ext

def get_page_stats(path, auto_ext=None):
    if auto_ext is None:
        auto_ext = []
    #cs_debug("get page stats: ",str(auto_ext))
    x = csm_tutor.compute_page_stats(globals(), cs_username, [cs_course] + path, ['question_info', 'state', 'actions', 'manual_grades'])
    qi = x['question_info']
    np = OrderedDict((i, j['csq_npoints']) for i,j in qi.items())

    bests = {k: 0 for k in qi}
    times = {k: None for k in qi}
    exts = {k: False for k in qi}
    raws = {k: 0 for k in qi}
    latenesses = {k: 0 for k in qi}
    late_by = {k: 0 for k in qi}
    # look through all actions, looking for the one that maximizes score
    for a in x['actions']:
        if a['action'] != 'submit':
            continue
        else:
            t = csm_time.from_detailed_timestamp(a['timestamp'])
            d = csm_time.from_detailed_timestamp(a['due_date'])
            for n in a['names']:
                if n not in bests:
                    continue
                try:
                    s = max(0.0, min(1.0, float(csm_tutor.read_checker_result(globals(), a['checker_ids'][n])['score'])))
                except:
                    continue
                edue = d + timedelta(seconds=get_extension(path, n, exts, auto_ext))
                l = late_penalty(qi[n], t, edue)  # this has to be here because of extensions
                real_score = s*l
                if real_score >= bests[n]:
                    bests[n] = real_score
                    raws[n] = s
                    latenesses[n] = l
                    times[n] = t
    # now, for manually graded problems, we need to look at both this person and their partner (if exists)
    for n, q in x['question_info'].items():
        if q['csq_grading_mode'] == 'manual':
            stime = x['state'].get('last_submit_times', {}).get(n, None)
            if True: # stime is None: # to handle people with double submissions
                # check partner
                mypartner = None
                try:
                    with open(os.path.join(cs_data_root, 'courses', cs_course, *path, '_partners.json')) as f:
                        pners = json.load(f)
                except:
                    pners = []
                for p1, p2 in pners:
                    if p2 == cs_username:
                        mypartner = p1
                        break
                    elif p1 == cs_username:
                        mypartner = p2
                        break
                if mypartner is not None:
                    stime2 = csm_cslog.most_recent(mypartner, [cs_course] + path, 'problemstate', {}).get('last_submit_times', {}).get(n, None)
                    if stime2 is not None and \
                           (stime is None or \
                            csm_time.from_detailed_timestamp(stime2) < csm_time.from_detailed_timestamp(stime)):
                        print('<b>', path[-1],  'using submission time from partner=', mypartner, stime2, '</b>')
                        stime = stime2
            if stime is not None:
                t = csm_time.from_detailed_timestamp(stime)
                s = 0
                for i in x['manual_grades']:
                    if i['qname'] == n:
                        s = float(i.get('score', 0.0))
                edue = d + timedelta(seconds=get_extension(path, n, exts, auto_ext))
                l = late_penalty(qi[n], t, edue)
                bests[n] = l*s
                late_by[n] = lb
                raws[n] = s
                times[n] = t
                latenesses[n] = l
    # finally, go through and set scores that were overridden.
    for n in np:
        for so in cs_user_info.get('score_override', []):
            if all(i==j for i,j in zip(so[0], path + [n])):
                bests[n] = so[1]
                raws[n] = so[1]
                latenesses[n] = None
    w_norm = sum(np.values())
    np = {k: v/w_norm for k,v in np.items()}
    names = list(qi)
    dnames = {i: qi[i].get('csq_display_name', i) for i in names}
    return {'time': times, 'raw': raws, 'late': latenesses, 'score': bests, 'weight': np, 'names': list(names), 'dnames': dnames, 'ext': exts, 'late_by': late_by}

def do_table(path, auto_ext=None, csv=False):
    if auto_ext is None:
        auto_ext = []
    x = get_page_stats(path, auto_ext)
    oprint = builtins.print
    def myprint(*args, **kwargs):
        if not csv:
            oprint(*args, **kwargs)
    p2 = '__'.join(path)
    bh = ""
    #print('<p>&nbsp;</p>')
    bh+='<center>'
    bh+='<table border="1">'
    bh+='<tr><td colspan="6" align="center"><b>%s</b> (<a onclick="toggle_details(\'%s\')" style="cursor:pointer;">show/hide details</a>)</td></tr>' % (path[-1].upper(), p2)
    bh+='<tr class="details_%s" style="display:none;"><th>Question</th><th>Weight</th><th>Submitted</th><th>Raw Score</th><th>Lateness Multiplier</th><th>Final Score</th></tr>' % p2
    o = 0.0
    for i in x['names']:
        ext = ' <small><font color="darkgreen">ext</font></small>' if x['ext'][i] else ''
        if x['weight'][i] == 0:
            continue
        bh+='<tr class="details_%s" style="display:none;">' % p2
        bh+='<td>%s</td>' % x['dnames'][i]
        bh+='<td>%.02f</td>' % x['weight'][i]
        bh+='<td>%s</td>' % ('None' if x['time'][i] is None else x['time'][i].strftime('%Y-%m-%d, %H:%M:%S'))
        bh+='<td>%.02f</td>' % x['raw'][i]
        bh+='<td>%s%s</td>' % (('%.02f%%' % (x['late'][i]*100)) if x['late'][i] is not None else 'N/A', ext)
        bh+='<td>%.02f</td>' % x['score'][i]
        o += x['weight'][i]*x['score'][i]
        bh+='</tr>'
    bh+='<tr><td colspan="5" align="right">Overall:</td><td>%.02f</td></tr>' % o
    bh+='</table>'
    bh+='</center>'
    return [o,bh]

def do_ex_table(path, auto_ext=None, csv=False):
    if auto_ext is None:
        auto_ext = []
    x = get_page_stats(path, auto_ext)
    oprint = builtins.print
    def myprint(*args, **kwargs):
        if not csv:
            oprint(*args, **kwargs)
    p2 = '__'.join(path)
    bh = ""
    #print('<p>&nbsp;</p>')
    bh+='<center>'
    bh+='<table border="1">'
    bh+='<tr><td colspan="6" align="center"><b>%s</b> (<a onclick="toggle_details(\'%s\')" style="cursor:pointer;">show/hide details</a>)</td></tr>' % (path[-1].upper(), p2)
    bh+='<tr class="details_%s" style="display:none;"><th>Question</th><th>Weight</th><th>Submitted</th><th>Raw Score</th><th>Lateness Multiplier</th><th>Final Score</th></tr>' % p2
    o = 0.0
    for i in x['names']:
        ext = ' <small><font color="darkgreen">ext</font></small>' if x['ext'][i] else ''
        if x['weight'][i] == 0:
            continue
        bh+='<tr class="details_%s" style="display:none;">' % p2
        bh+='<td>%s</td>' % x['dnames'][i]
        bh+='<td>%.02f</td>' % x['weight'][i]
        bh+='<td>%s</td>' % ('None' if x['time'][i] is None else x['time'][i].strftime('%Y-%m-%d, %H:%M:%S'))
        bh+='<td>%.02f</td>' % x['raw'][i]
        bh+='<td>%s%s</td>' % (('%.02f%%' % (x['late'][i]*100)) if x['late'][i] is not None else 'N/A', ext)
        bh+='<td>%.02f</td>' % x['score'][i]
        o += x['weight'][i]*x['score'][i]
        bh+='</tr>'
    bh+='<tr><td colspan="5" align="right">Overall:</td><td>%.02f</td></tr>' % o
    bh+='</table>'
    bh+='</center>'
    return [o,bh]




def total_lateness(pg, aext=[]):
    # this will be used to determine automatic extensions.  we'll see which
    # pages have the most lateness that could be removed by a 1-week extension.
    # this function will just sum weight*L for each question on the page, where
    # L is the number of points that would be earned back from a 1-week
    # extension.
    ostats = get_page_stats(pg)
    stats = get_page_stats(pg, aext)
    if 'ex' in pg[0]:
        cs_debug("checking ex")
        #cs_debug(ostats)
        #cs_debug(stats)
    o = 0
    for n in stats['names']:
        o += stats['weight'][n] * (stats['score'][n] - ostats['score'][n])
    return o
