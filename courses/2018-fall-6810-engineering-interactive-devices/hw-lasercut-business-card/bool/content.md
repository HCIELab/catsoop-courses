
For each of the expressions below, specify the resulting Boolean values in Python!

Remember to ask for help if you get stuck or ask us questions in class or office hours.)! Also your classmates and Google are awesome so make sure to use them too!!

<python>
csq_nsubmits = 2
qs = ["3 > 4",
"4.0 > 3.999",
"4 > 4",
"4 >= 4",
"2 + 2 == 4",
"True or False",
"False or False",
"not False",
"not not False",
"3.0 - 1.0 != 5.0 - 3.0",
"3 > 4 or (2 < 3 and 9 > 10)",
"4 > 5 or 3 < 4 and 9 > 8",
"not (4 > 3 and 100 > 6)"]

for q in qs:
    cs_print("<question pythonliteral>csq_prompt=\"<tt>%s</tt>\"\ncsq_soln=%r</question>" % (q+" ", eval(q)))

</python>

