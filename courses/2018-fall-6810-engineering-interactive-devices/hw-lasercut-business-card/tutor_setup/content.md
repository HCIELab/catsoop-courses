<python>
content_header = cs_long_name

atype='ajaxproblem'

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
        if y == 0:
            return x < closeness and x>-closeness
        else:
            return  abs((x-y)*1.0/y)<closeness
    return close


</python>

<h2>Site Background</h2>

For our course, we'll be using the online tutor website you're in right now.  The site is known as CAT-SOOP. CAT-SOOP is a browser-based open source education/classroom software developed and maintained by <a href="http://web.mit.edu/hartz/www/" target="_blank"> Adam Hartz</a> at MIT originally for use in one of MIT's introductory Electrical Engineering and Computer Science courses (<a href="http://sicp-s3.mit.edu/tutor/6.01" target="_blank">6.01</a>). The software is flexible so I started adapting it for use in several summer courses I teach. MOSTEC is one of them.  

What does CAT-SOOP stand for?  It stands for **C**AT-SOOP is **A**utomated **T**utor for **S**ix-**O**h-**O**ne **P**roblems.  You might go, "what?" that doesn't answer my question, and that's because it is a <a href="https://en.wikipedia.org/wiki/Recursive_acronym" target="_blank">recursive acronym</a>, which is considered funny by some.  Sometimes CAT-SOOP is just called "the tutor" by me, so if I do that in one of our discussions, please forgive me, and mentally make the translation or ask for clarification.

You'll be using CAT-SOOP for readings, testing your understanding (in a good low pressure way),  accessing links and outside resources, and carrying out software and hardware exercises. The sofware exercises exist in most parts of our exercises (homework, in-lab, etc...).  The hardware exercises will mainly happen in the Labs that take place throughtout the course. We'll address how to deal with hardware exercises starting in Lab 02.  For starters we'll just deal with basic CAT-SOOP question types.  

<h2>Questions</h2>
Let's give a question a try. Answer the multiple choice question. When you think you've got the right answer, press `Submit`. A little twirly think thing will come up and then hopefully you get a green 100%.  If you don't (give it a try) you get a 0% (that is red).

<question multiplechoice>
csq_soln = 'Correct Answer'
csq_options = ['Wrong Answer','Correct Answer']
csq_prompt = 'In general, you want to provide what sort of answer to a question?'
csq_nsubmits = float(10)
</question>

Here's another type of question: Numerical input. Give it a try.

<question pythonic>
csq_soln = 46
csq_prompt = 'What is 39 + 7?'
csq_check_function = is_close(0.01)
</question>

There may also be questions that have non-numeric answers. For example:

<question smallbox>
csq_soln = 'London'
csq_prompt = 'What is the capital city of England?'
csq_check_function = lambda x,y: x==y
</question>

<h3>Number of Tries</h3>

Sometimes you'll have infinite tries on a question, and sometimes you won't.  Pay attention so you don't waste them if you've got a finite amount. For example, note the problem below has infinite submissions...

<question pythonic>
csq_soln =  56**0.5
csq_prompt = 'What is the square root of 56? Enter your answer accurate to within 0.1%'
csq_check_function = is_close(0.001)
csq_nsubmits = float('inf')
</question>

...while the one below has only two.  Once you use up your last submission, that's it...no more. So use them wisely.

<question pythonic>
csq_soln = 34
csq_prompt = 'What is the decimal equivalent of the binary number 100010? (maybe use the internet if you don't know)'
csq_check_function = is_close(0.001)
csq_nsubmits = float(2)
</question>

<h3>Numerical Inputs</h3>
Civilizations have fallen because of rounding errors, and one of the things I'd like you to get lots of practice with is not rounding answers. This can be tricky since what if I ask you the following question:
<question pythonic>
csq_soln = 22.0/7
csq_prompt = 'What is the quotient when 22 is divided by 7?'
csq_check_function = is_close(0.0000001)
csq_nsubmits = float('inf')
</question> 

Now you may have had trouble with this question. How many decimal places do you need to put down? As it turns out, often you shouldn't need to worry about that, since most of the time you can either provide your answer as an expression.  For example, in the question immediately above, you can actually just put in `22.0/7` or `22/7`.  It will analyze it for you.   

<h3>Some Final and Additional Thoughts and Points</h3>
So, just to rehash: Each question offers a place to input your answer, and
several buttons:

* `Submit`: sends your answer to the server to be checked
for correctness.  You will be presented with information regarding the
correctness of your answer.  You will be allowed to a limited number of
submissions per question unless otherwise specified. After a submission, your answer will be givne a score. In the case of programming questions where your 
code might be partially correct/incorrect the *Show/Hide Detailed Results* button can give you specific details about which test cases you failed.

* `Save`: saves your current answer, but does not submit it for
checking or update your score.  This will remove any detailed
information provided from your last submission.
* `View Answer`: displays an answer written by the staff,
below the detailed results from your last submission.  **Viewing the
answer to a question will prevent any further submissions to that
question.**  

* Some questions have additional explanation available through a button
labeled "View Explanation," which becomes available after you have viewed the answer
for that question.

* Certain types of questions offer additional options.  For example, questions
that involve coding in Python typically offer a "Run Code" button that runs your
code and displays its output (or any error messages it produced) without scoring
your code and without using one of your limited number of submissions.

* Some questions will have hints that you can view.  You aren't penalized for viewing the hints, but try not to use them if you don't need to.
