<python>
show_due=False
doqueue=False
dopartners=False

labtitle="Welcome to Electronics"

atype="ajaxproblem"
import math
tutor.init_random()

r = cs_random.randint(100,500)
binops=['-','*','/']
cmpops = ['&gt;', '&lt;', '==', '&gt;=', '&lt;=', '!=']
boolops=['or','and']
types = ['float','int','noneType','bool']
short_types = ['float','int']


#submitted,solution
def list_check(x,y):
    return (len(x)==len(y)) and False not in [q[0]==q[1] for q in zip(x,y)]

def is_close(closeness):
    def close(x,y):
        return  abs((x-y)*1.0/y)< closeness
    return close


cs_scripts += '<script type="text/javascript" src="COURSE/scripts/scrollspy_builder.js"></script>'

csq_nsubmits = 10
</python>


<critical>You do NOT need to have Python installed to do these exercises, though it will certainly help! This first page is written so that if you want to you can use a Python environment.  You can do it on your personal computer if you already have Python3 installed, and I'd recommend this since I'd like all of us to have Python on our personal computers for ease of use, but you do not NEED to have Python on your computer. Otherwise just follow along.</critical>

<center>
<a href="https://www.youtube.com/watch?v=8lx711FflWw" target="_blank">Music for Lab</a>
</center>

<section>Getting Started</section>

For most of the class we're going to be working with the <a href="https://www.raspberrypi.org/products/raspberry-pi-2-model-b" target = "_blank">Raspberry Pi 3</a>, a powerful, single-board computer. The Raspberry Pi is just like most computers and smart phones that you're used to using (yes a smart phone is a computer), but it is special in a few ways. In particular, the "Pi" is way cheaper (~40 USD), and much more exposed to the world than other computers you have experience with. By "exposed" we mean both physically and from an interfacing point of view. Where a normal computer may only have a keyboard/mouse (or touchscreen) and screen and sound card for you to interact with, the Pi has all of that but also a lot more "raw" inputs and outputs which take a bit more effort to work with, but which also give us much more capability. This capability comes at a cost however...the Pi holds your hand a lot less than a normal computer... Where you might want to do something with your phone or computer and it would say, "No, I don't want to do that, I'm only supposed to do specific things" the Pi is pretty much down for whatever...you just need to know how to work with it and that's what we'll be focussing on in this class.

The Raspberry Pi is what we would term the <a href="http://en.wikipedia.org/wiki/Computer_hardware" target="_blank">hardware</a> of our system. In addition, in order to make a compute run, you need some <a href="http://en.wikipedia.org/wiki/Software" target="_blank">software</a>. Computers generally run a large piece of software known as an <a href="http://en.wikipedia.org/wiki/Operating_system" target="_blank">operating system</a> which we then run smaller programs within. On our Raspberry Pis, we're using the <a href="https://www.raspbian.org/" target="_blank">Raspbian</a> operating system which is a modified version of the <a href="http://en.wikipedia.org/wiki/Debian" target="_blank">Debian</a> Operating System that is itself a subvariant of the <a href="http://en.wikipedia.org/wiki/Linux_distribution" href="_blank">Linux</a> family of operating systems which are themselves a type of <a href="http://en.wikipedia.org/wiki/Unix" target="_blank"> GNU/Unix</a> family of operating systems. Other examples of operating systems are <a href="http://en.wikipedia.org/wiki/Microsoft_Windows" target="_blank">Windows</a>, <a href="http://en.wikipedia.org/wiki/Mac_OS" target="_blank">Mac OS</a>, <a href="http://en.wikipedia.org/wiki/Android_%28operating_system%29" target="_blank">Android</a>, and others. If you haven't worked with a Linux OS before don't worry. They are fun and cool to use, and you'll use it if you go into engineering in college so you might as well gain experience now. We'll spend some time today focussing on that.

Why don't we run one of the other Operating Systems?  Well part of the reason is that Raspbian and most Linux type OS's are free and maintained by a community of primarily volunteers. Windows or others would require we pay some money for licensing, and I'm not going to do that, so we're using Raspbian.  Even beyond that, Raspbian is an operating system that is optimized to run on the Raspberry Pi, and therefore for many tasks it works better than the others would. So while you might get a bit frustrated when trying to surf the web on your Pi and your download/upload rates are slow remember three things:

* The Pi wasn't meant to really browse the web, so just because it can doesn't mean it should
* Surfing the web on a Pi using Windows would be even worse
* The Pi cost 40 bucks
* The Pi is the size of a credit card
* The Pi is cool

You'll come to learn what to expect from the Pi as we move along. But first we need to figure out how to talk with it.  

<section>Working with the Pi</section>
So we have a general idea of what the Raspberry Pi is, but how will we be using it to do useful things?  It will be a two pronged approach:

* Learn how to connect, interface with, and interpret basic and complex electrical components to the Pi (requiring electrical engineering)

* Learn how to intrepret data, run calculations, make decisions, and generate outputs from the Pi (requiring computer science and programming)

These two tasks are super-intertwined...and part of Electrical Engineering and Computer Science (EECS) is managing both pieces. While you may specialize in one or the other during a career, ability to do both is very, very helpful.  So we'll be doing both in this class. We'll start with some programming today.

<section>Python 3</section>
The programming language of choice for us this summer is <a href="https://www.python.org/" target="_blank">Python 3</a>.  It is a fun language to learn, with a clear syntax, and it has lots of great pre-written pieces (libraries) that we can use. You can think of libraries as already working pieces of code that we can build upon (rather than writing everything from scratch).  Python is one of the top three or four most popular programming languages out there right now, and one which lots of computer science courses use at engineering schools (including MIT).  Even if you don't end up majoring in EECS, knowing how to program in a language like Python is invaluable for work in physics, health sciences, any field of engineering, social work, economics, and on and on...  It is a great life skill.

We'll be specifically learning Python 3, the newer Python (as opposed to Python 2).  Both version 2 and 3 are very similar, but there are subtle differences that will make things not work.  Keep this in mind!  Whenever you run Python, you'll need to make sure you're doing Python 3!!!

On a computer go to Menu>Programming>Python 3 (IDLE). A window should open up after a few seconds. This is IDLE and you'll be using it a lot this summer. 

IDLE is a Python environment that let's you run Python code.  It has a <b>shell</b> interface where you can type code "on the fly", but we'll mostly not use this.  Instead we'll create files and run them as stand alone code.  

Let's create a file. Go to File>New

 type <codep>x=5</codep> and then add <codep>print(x)</codep>. You should see the number <codep>5</codep> appear.  This is because <codep>x</codep> has been declared as a <b>variable</b> with value 5 inside of the Python environment.  

Let's do another one.  Create a variable called `y` and assign it a value of `13`.  Verify that when you type just `y`, it'll show up.  

Now let's do some math.  Type in `x+2*y`.  What do you think will be returned?  Go ahead and check.  You should see the correct answer.  

<subsection>Primitives</subsection>
 
Programming in general is pretty much just moving and manipulating data...and data is really anything: images, videos, words, numbers, thoughts, questions, answers...really anything. We need to express that data in certain forms however and there are certain rules and restrictions with how we work with these. We'll go over three common Python primitives below:

<subsection>Numbers</subsection>
Numbers can be integers or floats (known as `int` or `float`).  Integers are just like you've learned in math class...whole numbers that are positive negative, or zero.  Floats are all numbers (fraction numbers, whole numbers, etc...)  <b>Very importantly even though two variables may have numerically equivalent values such as:</b>
```
>>> x = 5
>>> y = 5.0
```
Python will still think of these two value as slightly different, and there are certain places where you'll only be able to use the integer version of a number rather than a float version.

<subsection>Strings</subsection>
Another data type in Python is the string. It can be used to hold a string of characters (which can include numbers...but which don't represent numbers). Here's how to declare a string:
```
>>> x = 'Cats'
>>> x 
'Cats'
```
Strings can be indicated by either single (`'`) or double (`"`) quotes (you just need to make sure you open and close with the same type).

<subsection>Booleans</subsection>

The last data type we'll be thinking about (for now anyways) is the boolean or `bool`. This is a data type that can either be the value `True` or `False` (capital `T` and `F` in Python!). Anytime we need to express a "yes/no" situation we'll be using a `bool` either explicitely or implicitely.  You actually use them all the time in your mind when you make decisions...(should I eat the rest of these Girl Scout Cookies?  Yes or No?  Probably Yes.) To make a `bool`, you can do:

```
>>> x = True
```

Usually in life `bools` are produced for us via some sort of operation (a comparison or test of equivalence or threshold test). To implement these tests we need <b>operators</b>

<subsection>Other Data Types</subsection>

We call the data types just discussed primitives, and they (among several others) form the basis of everything we do in Python.

<section>Operators</section>

In Python the "verbs" of our language are known as operators. They "operate" upon the data, including the primitives up above. These are generally expressed by certain symbols.  For example `+` means a different thing when done to two strings than when it is done to two numbers.

The following is a list of operators:

* `+`
* `-`
* `*`
* `/`
* `//`
* `**`
* `%`
* `==`
* `!=`
* `+=`
* `-=`
* `<`
* `>`
* `<=`
* `>=`
* `%=`
* `**=`
* `and`
* `or`
* `not`

Through experimentation in the Python terminal see what each of these operators does between different primitives (try numbers, strings, and booleans). For example, try things like doing a `string` + `string` and reassigning it to a new `string`.  If you aren't clear on what we're asking, post on the forum and we'll chat! Also see what happens when you try to use these operators on **different** data types (a `bool` and and `int`). You'll notice some operators don't make sense when used on certain data types and errors will be thrown (in red text). Read these errors since they'll help you learn! 

<subsection>Combinations</subsection>

As a little practice, answer the following questions about data types and operators below. 

<python>
z = [      
('int', '''<tt>%d + %d</tt>&nbsp;&nbsp;''' % (cs_random.uniform(-100,100),cs_random.uniform(-100,100))),
('float','''<tt>%.01f + %d</tt>&nbsp;&nbsp;''' % (cs_random.uniform(-100,100),cs_random.uniform(-100,100))),
('float','''<tt>%d + %.4f</tt>&nbsp;&nbsp;''' % (cs_random.uniform(-100,100),cs_random.uniform(-100,100))),
]

for i in z:
    cs_print('<question multiplechoice>\ncsq_options=types\ncsq_soln=%r\ncsq_prompt=%r\n</question>' % i)

x = [

('int', '''<tt>%d %s %d</tt>&nbsp;&nbsp;''' % (cs_random.uniform(-100,100),cs_random.choice(binops),cs_random.uniform(-100,100))),
('float','''<tt>%f %s %d</tt>&nbsp;&nbsp;''' % (cs_random.uniform(-100,100),cs_random.choice(binops),cs_random.uniform(-100,100))),
('float','''<tt>%d %s %.08f</tt>&nbsp;&nbsp;''' % (cs_random.uniform(-100,100),cs_random.choice(binops),cs_random.uniform(-100,100))),
('float','''<tt>%d %s %d.</tt>&nbsp;&nbsp;''' % (cs_random.uniform(-100,100),cs_random.choice(binops),cs_random.uniform(-100,100))),
('bool','''<tt>%d %s %d</tt>&nbsp;&nbsp;''' % (True,cs_random.choice(boolops),False)),
('bool','''<tt>%f %s %d</tt>&nbsp;&nbsp;''' % (cs_random.uniform(-100,100),cs_random.choice(cmpops),cs_random.uniform(-100,100))),
('bool','''<tt>%d %s %.08f</tt>&nbsp;&nbsp;''' % (cs_random.uniform(-100,100),cs_random.choice(cmpops),cs_random.uniform(-100,100))),
        ]

cs_random.shuffle(x)

for i in x:
    cs_print('<question multiplechoice>\ncsq_options=types\ncsq_soln=%r\ncsq_prompt=%r\n</question>' % i)
</python>

<python>
x = [cs_random.randint(1,20) for i in range(20)]
f = [cs_random.uniform(1,20) for i in range(20)]

x[5] = cs_random.randint(4,10)
x[4] = cs_random.randint(3,8)*x[5]+1

x[6] = cs_random.randint(2,8)
x[7] = cs_random.randint(2,8)
x[8] = cs_random.randint(2,8)

x[10] = cs_random.randint(2,20)
x[9] = 2*x[10]+1

x[13] = cs_random.randint(1,20) + cs_random.randint(6,9)/10.

if f[3]>3:
    f[3] = cs_random.uniform(0.5,3.0)

def numeric_check(x, y):
    return type(x)==type(y) and abs(x-y)<=1e-3
</python>

<subsection>More Practice</subsection>

For each of the expressions below, specify its value.  Be careful of types! If something doesn't make sense...don't just go 'iunno' and move on! 
 
<python>
qs = [
('''<tt>%d + %d - %d</tt>&nbsp;&nbsp;''' %(x[0],x[1],x[2]), x[0]+x[1]-x[2]),
('''<tt>%.1f * %.1f</tt>&nbsp;&nbsp;''' %(f[0],f[1]), round(f[0],1)*round(f[1],1)),
('''<tt>- - %d</tt>&nbsp;&nbsp;''' % (x[3]), x[3]),
('''<tt>%d // %d</tt>&nbsp;&nbsp;''' %(x[4],x[5]), x[4]//x[5]),
('''<tt>%.1f / %.1f</tt>&nbsp;&nbsp;''' %(x[4],x[5]), float(x[4])/x[5]),
('''<tt>(%d + %d) * %d</tt>&nbsp;&nbsp;''' %(x[6],x[7],x[8]), (x[6]+x[7])*x[8]),
('''<tt>%d + %d * %d</tt>&nbsp;&nbsp;''' %(x[6],x[7],x[8]), x[6]+x[7]*x[8]),
('''<tt>%d ** %d + %d</tt>&nbsp;&nbsp;''' %(x[0],x[1],x[2]), x[0]**x[1]+x[2]),
('''<tt>%.1f ** %.1f</tt>&nbsp;&nbsp;''' %(f[2],f[3]), float(round(f[2],1))**round(f[3],1)),
('''<tt>%d + %.1f</tt>&nbsp;&nbsp;''' %(x[11],x[12]), float(x[11]+x[12])),
('''<tt>%d // %d == %d / %.1f</tt>&nbsp;&nbsp;''' %(x[9],x[10],x[9],x[10]), False),
('''<tt>round(%f)</tt>&nbsp;&nbsp;''' %(x[13]), int(round(x[13]))),
('''<tt>int(%.1f)</tt>&nbsp;&nbsp;''' %(x[13]), int(x[13])),
('''<tt>%d * %d == %d * %.1f</tt>&nbsp;&nbsp;''' %(x[14],x[15],x[14],x[15]), True),
]

for q in qs:
    p,s = q
    cs_print("<question pythonliteral>\n%s\ncsq_prompt=%r\ncsq_soln=%r\n</question>" % ("csq_check_function=numeric_check" if not isinstance(s,bool) else "", p, s))
</python>


<section>Functions</section>

So we're starting to see that we can generate outputs in a way very similar to a calculator with Python. For example, if someone wanted us to figure out what 6 plus four times a number is and we wanted to do that for the number five we could do:

```
>>> 6+4*5
    26
```
And then if we wanted to know what it was for 19 we'd have to do:
```
>>> 6+4*19
    82
```
And so on and so on for every number we want to do this on.  Instead we can use variables to abstract this operation away for us...therefore the operation doesn't exist only as a series of numbers typed out, but can exist using variables.  Basically we want some way to express the following:
```
    Give me a value. I'll call it x.
    I will return to you 6 + 4*x
```
How do we do that? The answer is functions.

In Python you can create things called functions which are basically the same thing as algebraic functions. For example, let's say you wanted to Pythonically represent the following function which is the mathematical way of saying "Five times something"
$$ 
f(x) = 5x
$$

In Python you could do this by writing:
```
def f(x):
    return 5*x
```
Then once this function was written you could do:
```
>>> f(5)
    25
>>> f(19)
    95
```

`def` stands for "definition", which is what we're doing here...we're defining a function.  `f` is the name of the function, the parentheses demarcate the inputs to the function (in this case a variable called `x`.  And the `return` line indicates what the function returns (spits back out!)

How do we write and deploy this function? Normally you'll write it in a `.py` file (short for "python") and this is how we'll want you to be writing most of your code! 

To create a python file, in IDLE, go to File>New File.  This will open up a blank page where we can write Python scripts.  Before we forget, let's save this file as `lab01py`.  

Once that is done, let's create our first function. Type the following into the window:
```
def f(x):
    return 5*x
```
Now as you type it, you should notice the indent. Pay attention to the spaces! Python sorts itself out using spacing so that `return` line needs to be 4 spaces or a Tab over from where the `def` line is at.  The Python terminal should auto-indent for you, but always be aware of that since sometimes it might not be what you want. You cannot mix spaces and tabs in your indents. Python will get sad.  So when you're writing code, make sure to use one or the other.

When you've typed in that function, go up to Run>Run Module or by pressing F5. Your function is now defined and active in the Python terminal (the part with the `>>>` markers) so go back down to there and  try a few function calls. For example, typing:
```
>>> f(6)
```
should result in a:
```
    30
```
Similarly you'll get this:
```
>>> f(-2)
    -10
```
and so on....


This is great. It is much easier to build something once and use it many times. Here's another example of a function.
```
def howManyFives(t):
    return t//5
``` 
So in code when we call this function we can get:
```
>>> howManyFives(34)
    6
>>>
```
We can also store the value returned by a function into a variable. For example:
```
>>> y = howManyFives(26)
>>> print(y)
    5
>>>
```

`print` is another function that will print out the value of a variable or expression if desired.  

Note that python doesn't automatically spit out the return value if there is a variable there to catch the return value.

Now the super neat thing is that if a function returns an *int* like our `howManyFives()` function does, then when we call it we can treat it sort of like an integer.  For example, we can do this crazy thing:
```
>>> q = howManyFives(13) + 11
>>> print(q)
    13
```

Or even call the same function inside itself:
```
>>> w = howManyFives(howManyFives(103))
>>> print(w)
    4
```

In the example above, the inside call of `howManyFives()` returns a 20, which is then immediately fed into the input of the second (outer) <tt>howManyFives()</tt>.  Pretty cool, yes?  If you are not convinced you will be eventually.

<section>Function Types</section>

For each of the following functions, specify the type of the output, assuming
that valid input is provided (no Python error occurs).  If it can be either an
int or a float, use <tt>num</tt>, which isn't a real Python type, but which 
we'll use to indicate that either basic numeric type is legal. Try to deduce your way through it, but also feel free to experiment and test in the terminal!!

<question multiplechoice>
csq_prompt = """<pre>def a(x):
    return x+1</pre><p>Result:&nbsp;"""

csq_options = ['num','int','float','bool','noneType']
csq_soln = "num"
explanation = """If an <tt>int</tt> is passed in, then the result will be an <tt>int</tt>.  However, if a <tt>float</tt> is passed in, then the result will be a <tt>float</tt>."""
</question>

<question multiplechoice>
csq_prompt = """<pre>def b(x):
    return x+1.0</pre><p>Result:&nbsp;"""

csq_options = ['num','int','float','bool','noneType']
csq_soln = "float"
explanation = "Regardless of whether an integer or a float is passed in, the result will be converted to a float." 
</question>

<question multiplechoice>
csq_prompt = """<pre>def c(x,y):
    return x > y</pre><p>Result:&nbsp;"""

csq_options = ['num','int','float','bool','noneType']
csq_soln = "bool"
</question>

<question multiplechoice>
csq_prompt = """<pre>def d(x,y,z):
    return x >= y and x<=z</pre><p>Result:&nbsp;"""

csq_options = ['num','int','float','bool','noneType']
csq_soln = "bool"
</question>

<question multiplechoice>
csq_prompt = """<pre>def e(x,y):
    x + y - 2</pre><p>Result:&nbsp;"""

csq_options = ['num','int','float','bool','noneType']
csq_soln = "noneType"
</question>

<h3>Transcript</h3>
Assuming the functions in the last set of questions above have been defined (functions `a`, `b`, etc...), provide the value of the
expressions below (be careful of types!). 

If evaluating the expression would cause an error, write <tt><font color="blue">error</font></tt> in the
box.  If the value of an expression is a function, write <tt><font color="blue">function</font></tt> in the box.

<python>
def a(x):
    return x+1

def b(x):
    return x+1.0

def c(x,y):
    return x > y

def d(x,y,z):
    return x >= y and x<=z

def e(x,y):
    x + y - 2

qs = ["a(6)", "a(6.0)", "a(-5.3)",
      "a(a(a(6)))", "c(a(1), b(1))",
      "d(a(3), b(4), a(6))",]

for q in qs:
    cs_print("<question pythonliteral>\ncsq_prompt='<tt>%s</tt><br/>'\ncsq_soln=%r\ncsq_check_function=numeric_check</question>" % (q,eval(q)))
</python>

<question smallbox>
csq_soln="error"
csq_prompt = "<tt>e(1,2,3)</tt><br/>"
csq_check_function = lambda x,y: x.strip().lower()==y.strip().lower()
</question>


<section> Writing Some Functions</section>

Let's now get a bit of experience writing some functions. Write a python function `m(x)` that expresses (returns) the algebraic function:
$$
m(x) = 15x^2 -3x +11
$$

Enter your code and submit it below. Use the <a href="http://www.skulpt.org/" target="_blank">online Python environment</a> or your local version of Python for testing/experimenting.

*The `pass` statement below should be removed by you when you write your code. Its presence is required by Python in order to provide you with an empty code "skeleton" when defining the function.*

<question pythoncode>
values = [cs_random.randint(-100,100)*0.34 for x in range(6)]

csq_initial = '''def m(x):
    pass
'''
csq_soln = '''def m(x):
    return 15*x**2 -3*x + 11
'''
csq_tests = [
{'code':'ans= m(%s)' %(q)} for q in values]      
csq_tests.append({'code':'ans=m(0)'})

</question>

<subsection>Function with two inputs</subsection>

<python>
terms = tuple(cs_random.randint(1,14) for x in range(5))
values = [tuple(cs_random.randint(-100,100)*0.34 for t in range(2)) for x in range(6)]
</python>
Write a function that implements Pythonically the multivariable mathematical expression $n(x,y)$:
$$
n(x,y) = @{terms[0]}x^3 + @{terms[1]}x^2y - @{terms[2]}y^2 - @{terms[3]}x + @{terms[4]}
$$

<question pythoncode>
csq_initial = '''def n(x,y):
    pass
'''
csq_soln = '''def n(x,y):
    return %s*x**3 + %s*x**2*y - %s*y**2 - %s*x + %s
''' %terms
csq_tests = [
{'code':'ans= n(%s,%s)' %q} for q in values]      
csq_tests.append({'code':'ans=n(0,0)'})

</question>

<subsection> Function Calling another Function</subsection>

Now let's write a Python function that is defined as the following:
$$
r(t) = n(t,m(t))
$$ 
where the functions $n$ and $m$ are as defined above.  You can assume that `m(x)` and `n(x,y)` are already defined and working for you in this problem.
<python>
val = [cs_random.randint(-100,100)*0.34 for x in range(6)]
</python>

<question pythoncode>

csq_initial = '''def r(t):
    pass
'''
csq_code_pre = '''def n(x,y):
    return %s*x**3 + %s*x**2*y - %s*y**2 - %s*x + %s
def m(x):
    return 15*x**2 -3*x + 11

''' %terms


csq_soln = '''def r(t):
    return n(t,m(t))
'''

csq_tests = [{'code':'ans= r(%s)' %(q)} for q in val]      
#csq_tests = []
csq_tests.append({'code':'ans=r(0)'})

</question>

<section>Strings and Functions</section>

Functions can also handle strings.  Below, write a function called `full_name` that takes in two inputs `first_name` and `last_name` (both strings) and responds with a greeting like the following:

```
>>> full_name('Richard','Nixon')
    Hello, Richard Nixon! 
```

*Your code should return the message, correct with the proper punctuation and spacing*

 
<question pythoncode>
csq_soln = '''def full_name(first_name, last_name):
    return 'Hello, ' + first_name + ' ' + last_name + '!'
'''
csq_initial = '''def full_name(first_name,last_name):
    pass'''
csq_tests = [{'code':'ans= full_name("Joe","Steinmeyer")'},{'code':'ans= full_name("Blanky","McBlankenstein")'},{'code':'ans= full_name("Reimi","Hicks")'}]      

</question> 


<section>Booleans and Functions</section>

Functions can also take in Booleans (variables that are either True or False...or the value True/or False).  In Python 0 is equivalent to False and everything else is equivalent to True.  So `7` is `True` as is the word `ocelot`.  This is sort of weird but just something to keep in mind.

We can perform logical operations on booleans using the `not`, `and`, and `or` operators.  These perform fundamental logical operations as described in standard <a href="https://en.wikipedia.org/wiki/Truth_table" target="_blank">Truth Tables</a>.  For example in the Python shell you can try the following:
```
x=True
y=False
z = x and y #z will become False since True and False is False
q = x or z #will become True since True or False is False
h = not q #will become False since not True is False
```

Below I want you to write a function called `NAND_3` that takes in three inputs and evalutes the boolean operation not (input1 and input2 and input3).  Boolean math has order of operations just like normal person math, so things inside the parentheses should be evaluated first.  Write the function and see how it looks below:

<question pythoncode>
csq_soln = '''def NAND_3(i1,i2,i3):
    return not(i1 and i2 and i3)
'''
csq_initial = '''def NAND_3(i1,i2,i3):
    pass
'''
csq_tests = [{'code':'ans= NAND_3(True,True,True)'},
{'code':'ans= NAND_3(False,True,False)'},
{'code':'ans= NAND_3(False,False,False)'},
{'code':'ans= NAND_3(False,False,True)'},
{'code':'ans= NAND_3(True,True,False)'},
{'code':'ans= NAND_3(True,True,"cat")'}]

</question> 

