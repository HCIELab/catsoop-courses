<python>
cs_scripts += '<script type="text/javascript" src="COURSE/scripts/scrollspy_builder.js"></script>'
</python>
<style>
table, td, th {
    text-align:center;
}
</style>

<script type="text/javascript">
var toggle_details = function(path){
    $('.details_' + path).toggle();
}

</script>

<python>
<include>_grades.py</include>

import os
with open(os.path.join(cs_data_root, 'courses', cs_course, 'progress', '_auto_extensions.csv')) as f:
    auto_ext = f.read()
    auto_ext = dict(i.split(',', 1) for i in auto_ext.splitlines())
    auto_ext = {k: list(map(int, v.strip().split(','))) for k, v in auto_ext.items()}
    auto_ext = auto_ext.get(cs_username, [])

print('<section>Automatic Extensions</section>')

#print("Automatic Extensions are almost deployed (The page might crash until I finish).")

cs_print("Scores on this page have been rounded to four places after the decimal. In computation of final grades, rounding will not be carried out at intermediate steps.")
if auto_ext == []:
    print('No automatic extension information recorded.')
elif len(set(auto_ext)) == 1:
    print('As of right now, your automatic extensions will both be applied to week %d.' % auto_ext[0])
else:
    print('As of right now, your automatic extensions will be applied to weeks %d and %d.' % (auto_ext[0], auto_ext[1]))
is_csv = cs_form.get('csv', '0') == '1'

names = ['username']
fields = [cs_username]
</python>


<python>
lab_tables = []
weight = 1.0/len(labs)
lab_scores=[]
lab_score = 0.0
for i in labs:
    x = do_table([i], auto_ext)
    lab_tables.append(x[1])
    lab_scores.append(x[0])
    names.append(i)
    fields.append(x[0])
    lab_score+= weight*x[0]
cs_print("<section>Labs (Score: {}%)</section>".format(round(lab_score*100,1)))
for t in lab_tables:
    cs_print(t)

</python>




<python>
titles = []
big_ex_list = []
overall_overall_score = 0.0
weight = 1.0/len(exercises)
for week in exercises:
    nameo = all_608_exes[week][2]
    exes = all_608_exes[week][0]
    weights = all_608_exes[week][1]
    week_sum = sum(weights)
    norm_weights = [i/week_sum for i in weights]
    tables = []
    ovallsc = []
    iter = 0
    overall_score = 0
    for i in exes:
        x = do_ex_table([week,i], auto_ext)
        tables.append(x[1])
        ovallsc.append(x[0])
        names.append(i)
        fields.append(x[0])
        overall_score+= x[0]*norm_weights[iter]
        iter+=1
    big_ex_list.append(tables)
    titles.append("<center><h3>{} (Score: {}%)</h3></center>".format(nameo,round(overall_score*100,1)))
    overall_overall_score += weight*overall_score

cs_print("<section>Exercises (Score: {}%)</section>".format(round(overall_overall_score*100,1)))
for i in range(len(exercises)):
    cs_print(titles[i])
    for t in big_ex_list[i]:
        cs_print(t)

</python>


<python>
import csv

def dex_getter(file,kerberos):
    try:
        with open(file) as csvfile:
            score_reader = csv.reader(csvfile)
            for row in score_reader:
                if kerberos in row[0]:
                    return [1,float(row[1]),row[4],row[6]]
            return [-1,0,0]
    except:
        return [0,0,0]
file_base = '/home/catsoop/catsoop12data/courses/spring18/dexgrades/'
site_base = "https://iesc-s2.mit.edu/608/spring18/"
dexes = {"Exercise 02: Watch": "ex02.watch",
        "Exercise 03: Etch-a-Sketch": "ex03.etch_sketch_send_retrieve",
        "Exercise 03: Ball-Launch": "ex03.ball_launch",
        "Exercise 04: Weather": "ex04.weather",
        "Exercise 05: Trivia Game": "ex05.trivia_game",
        "Exercise 05: Treasure Hunt": "ex05.treasure_hunt",
        "Exercise 06: Temperature Sensor": "ex06.temperature_sensor",
        "Exercise 06: The Clapper": "ex06.the_clapper",
        "Exercise 07: Bop-It": "ex07.bopit",
        "Exercise 07: Battery-Reporting": "ex07.long_term_reporting",
        "Exercise 08: Key Exchange Implementation": "ex08.keimplement",
        "Exercise 08: Cards": "ex08.cards",
}
done = []
dex_scores = []
kerberos =  cs_user_info['username']
for dex in dexes:
    #look up dex
    dex_stuff = dex_getter(file_base+dexes[dex]+".csv",kerberos)
    spot = dexes[dex].replace(".","/")
    #if there is a grade there:
    if dex_stuff[0]==1:
        dex_scores.append(float(dex_stuff[3]))
        done.append('''<li>{}/{}  <a href="{}{}" target="_blank">{}</a></li>'''.format(float(dex_stuff[3]),2.5,site_base,spot,dex))
total_dex_score = min(sum(dex_scores),10)
num_dexes = len(dex_scores)
cs_print("<section>Design Exercises (Score: {}%)</section>".format(round(total_dex_score*10,1)))
if num_dexes == 0:
    cs_print("You have submitted 0 Design Exercises for a total of 0/10.0 points:")
elif num_dexes == 1:
    cs_print("You have submitted {} Design Exercise for a total of {}/{} points:".format(num_dexes,total_dex_score,"10.0"))
else:
    cs_print("You have submitted {} Design Exercise for a total of {}/{} points:".format(num_dexes,total_dex_score,"10.0"))
cs_print("<ul>")
for d in done:
    cs_print(d)
cs_print("</ul>")

</python>
* Note the number of submitted design exercises will lag submission date by approximately one week to allow for manual grading.

<python>

mt = '/home/catsoop/catsoop12data/courses/spring18/progress/mtt.csv'
exam_score = -1
with open(mt) as csvfile:
    score_reader = csv.reader(csvfile)
    for row in score_reader:
        if kerberos in str(row[0]):
            exam_score = float(row[7])
            break

if exam_score != -1:
    cs_print("<section>Midterm (Score: {}%)</section>".format(round(exam_score,1)))
    cs_print("""Your score on the exam was {} out of 100.0 points. 

You can pick up your exam for review in class or office hours starting Tuesday April 17th in Office hours and in any staffed class hours afterwards. If you would like to submit for a regrade you can do so up until/including April 24th. When submitting a regrade request, please attach a short, several-sentence note to the exam explaining why. If it is a matter of point-tallying, we may do that on the spot with you if possible. If it is a request to regrade a problem/problems, first be aware that the staff may regrade the entire exam, and second please be as clear as possible in your request.""".format(round(exam_score,1)))
else:
    cs_print("<section>Midterm (Score: No Score)</section>")
    cs_print("""There is not a midterm score recorded for you. If you believe this is an error, email jodalyst@mit.edu.""")
</python>

<b>Exam Statistics:</b>

* Mean: 70.7
* Median: 72.0
* Standard Deviation: 15.1

<python>
'''
<figure>
  <p><img src="CURRENT/5point_hist.png" width="500"/>
  <figcaption>Class Performance Distribution with 5-point resolution</figcaption>
</figure>


<figure>
  <p><img src="CURRENT/1point_hist.png" width="500"/>
  <figcaption>Class Performance Distribution with 1-point resolution</figcaption>
</figure>
'''
</python>
