<python>
content_header = cs_long_name

atype='ajaxproblem'
nchecks=2

viewsoln = False

tutor.init_random()

r = cs_random.randint(100,500)
binops=['-','*','/']
cmpops = ['&gt;', '&lt;', '==', '&gt;=', '&lt;=', '!=']
boolops=['or','and']

def test_equiv(x,y):
    if len(x) != len(y):
        return False
    for q in range(len(y)):
        if y[q] not in x:
            return False
    return True

def test_close(x,y):
    return abs(float(x)-float(y))*1.0/(1.0*abs(float(x)))<=0.01

#submitted,solution
def list_check(x,y):
    return (len(x)==len(y)) and False not in [q[0]==q[1] for q in zip(x,y)]

def is_close(closeness):
    def close(x,y):
        return  abs((x-y)*1.0/y)<closeness
    return close

</python>


While we'll be working with our Raspberry Pi's (which need their own setting up) it would probably really be beneficial for you to have a working version of Python 3 on your computer.  Go to <a href="https://www.python.org/downloads/" target="_blank">Python Main Site</a> and download Python3 for your computer based on what operating system you have. 

<subsection>Windows Issues</subsection>
<div class="critical">Carefully read the instructions as it is downloading!! Windows users in particular make sure to check the Add-to-Path option when it shows up. Post on the forum if you run into any problems!</div>

<subsection>Apple Issues</subsection>

Mac OSX by default comes with Python 2.7. We are not using this version in MITES Electronics. Python2 is the past and Python3 is the future.  No arguments, friend.

<subsection>Linux Issues</subsection>

Most Linux/Unix distributions come with Python 2.7.  We are not using this version in MITES Electronics. If you're using Linux/Unix, I'm guessing you know what you're doing, but if not, let me know if you run into issues...it should be as easy to setup as the other OS's (if not easier, honestly).

<section>Where do I edit my Code?</section>

Python is a "pretty language" (nice to look at opposed to something like C/C++ or Java), but part of the reason for this is that it relies on tabs and spacing for indicating blocks/regions/control structures.  This makes it incompatible with something like Microsoft Word or something like that.  Instead you should use IDLE 3 (Possibly known as just IDLE if your compy hasn't had Python before).  This is a nice Python-focussed editor that will help you along as you write code (indent for you, highlight stuff, be your friend).  So use this! Ask questions if you're having trouble getting this set up.

<center>
<iframe width="560" height="315" src="https://www.youtube.com/embed/YziUwPFO6JY" frameborder="0" allowfullscreen></iframe>
</center>

Note(!): There are also other editors out there, (Sublime Spyder, Eclipse, Python Notebooks, etc...)

