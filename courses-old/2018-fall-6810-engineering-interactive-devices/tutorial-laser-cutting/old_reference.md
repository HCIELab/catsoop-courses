<!--- One day we should delete all this! -->

<figure>
  <p><img src="CURRENT/breakout.jpg" style="width:3in" />
  <figcaption>A reminder of the breakout board</figcaption>
</figure>

In the photo above, two wires are used to connect the `3V3` pin and the `GND` pin of the Raspberry Pi to the + left rail and the - left rail of the breadboards.  The `3V3` pin is positive voltage (of 3.3V). The `GND` is. Very often it is a good idea to use the really long nodes on both sides of the breadboard as a way to distribute power and ground across the breadboard so you don't need to use really long wires all the time.

**when we draw out the breakoutboard in this lab and later labs we'll often just represent it as a gray box.**

<section>Using an LED as an output</section>

OK so now let's grab a LED and hook up the LED to the output of GPIO4 as shown below. You may remember from Lab 01 that we should never hook up an LED to power without some resistor in series like shown below:

<figure>
  <p><img src="CURRENT/circ_build1.jpg" width="20%"/>
  <figcaption>A reminder about how to use LEDs</figcaption>
</figure>

It turns out that our Raspberry Pi's have an built-in resistor (shown in figure below) that let's us not need to add one ourselves when interfacing with the GPIO pins.

<note>This is only because we've included an extra protection shield on the board. A Raspberry Pi off of the streets, will not have this, so if you're using your own hardware you'll need to include your own resistors.</note>

This in-built protection is only for the GPIO pins...not the 3.3V pins (`3V3`) or other pins) Try to hook the LED up in the correct direction and to the right pins. (Long leg to GPIO Pin 4 which is represented by the `#4` label and the short leg of the LED to ground!

<figure>
  <p><img src="CURRENT/LED_with_Pi.png" style="width:3in" />
  <figcaption>Connecting an LED to the Pi.</figcaption>
</figure>

When you think you've added the part correctly, open a new file in Python (File>New) and then copy-paste the code below into that file.  Once it is there, save it, and then run it by either going to Run>Run Code or pressing F5 on the keyboard (cool kids press F5).

<pre class="prettyprint linenums lang-python">
#Simple LED Flasher
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

led_pin = 4 #pin we'll use for the LED

GPIO.setup(led_pin,GPIO.OUT)
GPIO.output(led_pin,0)

time_pause = 0.25 #how long a standard pause is in this program

GPIO.output(led_pin,1)
time.sleep(time_pause)
GPIO.output(led_pin,0)
time.sleep(time_pause)
GPIO.output(led_pin,1)
time.sleep(time_pause)
GPIO.output(led_pin,0)
time.sleep(time_pause)
GPIO.cleanup()
</pre>

<question pythonic>
csq_prompt="When you run the code how many times does the LED flash?"
csq_soln = 2
</question>

Let's go through line-by-line what this code is doing.

In Python any line or part of a line that begins with a `#` is a comment, meaning it is meant for human reading.

The two lines below grant us access to other pieces of pre-written Python code.  The first one gives us access to some Python "libraries" that let us interact with the actual Raspberry Pi hardware<footnote>GPIO stands for "General Purpose Input-Output"</footnote> and what we're doing here is importing the `RPi.GPIO` library and just calling it `GPIO` for short.  When we want to use a part from this library we'll access it by doing `GPIO.thing`  The second line imports the `time` library which gives us access to the `sleep` function which we'll use to add pauses in our program.

<pre class="prettyprint linenums lang-python">
import RPi.GPIO as GPIO
import time
</pre>

<subsection>Setup</subsection>

These two lines configure the GPIO library so we can use it. That's about all you need to know for now:

<pre class="prettyprint linenums lang-python">
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
</pre>

<subsection>Setting Up Pins to Be Outputs</subsection>

To make life easy it is better to use variables wherever possible.  What we'll do is create a variable called <codep>led_pin</codep> and assign a value of <codep>4</codep> to it.  Then we can use that anywhere we want to refer to the LED.  In the future if we want to change what pin we use for the LED we only need to change that number in one spot as a result.

Here we do our first pin-specific action for the LED. We set up Pin 4 to be an output (pins can be either inputs or outputs...to control an LED that means we need it to be an output).

<pre class="prettyprint linenums lang-python">
led_pin = 4
GPIO.setup(led_pin,GPIO.OUT)
</pre>

<subsection>Turning On/Off, Pausing</subsection>

We then have a bunch of lines that look like the following. The first type of line tells the corresponding pin (dictates by the variable <codep>led_pin</codep> which has a value of <codep>4</codep> in this case) to be ON (1 or True == High OUTPUT which makes the LED go on), (0 or False == Low OUTPUT which makes the LED go off)  The second line (<codep>time.sleep(time_pause)</codep>) has the program pause for 0.25 seconds because it is saying to sleep the computer <codep>time_pause</codep> amount where <codep>time_pause</codep> is another variable we specified in our code!


<pre class="prettyprint linenums lang-python">
GPIO.output(led_pin,1)
time.sleep(time_pause)
GPIO.output(led_pin,0)
time.sleep(time_pause)
GPIO.output(led_pin,1)
time.sleep(time_pause)
GPIO.output(led_pin,0)
time.sleep(time_pause)
</pre>

<subsection>Cleanup</subsection>

Finally the following line makes sure we shut down our hardware access ok.  Just like you don't want to just unplug a running computer, sometimes you don't want to just stop controlling the outputs of the Raspberry Pi.  This function call will make sure we end our time in Python gracefully.

<pre class="prettyprint linenums lang-python">
GPIO.cleanup()
</pre>



<section>Red, White, and Blue (or other colors)</section>

<subsection>Assignment 1</subsection>

Now go and grab three LEDs from the parts supply, and using the previous starter code as a starting point, create code that turns on each LED in sequence, then turns them off, and repeates this pattern three times.  Use GPIO (#) pins 4, 17, and 27 ONLY!

<figure>
  <p><img src="CURRENT/rwb_circuit.png" style="width:5in" />
  <figcaption>Building a Red, White, and Blue Circuit</figcaption>
</figure>


When you feel confident that you've built the circuit correctly and have code working properly, show a staff member and then submit your working code below for record keeping.

<question bigbox>
csq_soln = "Code that works!"
csq_nsubmits = 50
csq_check_function= lambda x,y: True
</question>
<subsection>Assignment 2: Code Modification</subsection>

We'd now like you to make two LEDs turn on together for 0.5 seconds, while the other LED is off, and then flip it (two LEDs off and the other on for 0.5 seconds), and I want this repeated ten times.  Try and use a `for` loop to do this

When it is working, show a staff member and then submit your code below for record keeping:
<question bigbox>
csq_soln = "Code that works!"
csq_nsubmits = 50
csq_check_function= lambda x,y: True
</question>

<subsection>Assignment 3: Another Code Modification</subsection>

Now make one LED (pick one...it is up to you) flash at 10 Hertz using a <codep>for</codep> loop.  Don't know what that means?  Better look it up.  When working show a staff member.

<section>Inputs</section>

We just saw that we can control electrical signals with our Pi (and make LEDs go on and off). We can also have our Pi be sensitive to externally generated electrical signals.  We'll start investigating this ability by looking at switches which we used last week. As a refresher:

<subsection>Switch</subsection>
<center>
<img src="CURRENT/switch.png" width="15%" />
</center>

<figure>
  <p><img src="CURRENT/switch.png" width="15%" />
  <figcaption>Switches</figcaption>
</figure>

There are many, many types of switches, and you'll gain some experience with them. What they all do, however is selectively control the flow of electricity.  For today's lab we'll be using what are called "Normally Open Momentary" switches.  This means that when left untouched, the two terminals of the switch are disconnected, but when you press on the button, the two terminals connect.  In real life our switches look like what is shown in the figure below, where we've also provided an image of the switch in the context of the breadboard. 

<figure>
  <p><img src="CURRENT/switch_hookups.jpg" width="45%" />
  <figcaption>Refresher from Lab 01</figcaption>
</figure>

You can plug your switch into the breadboard as shown above. 

**Pay attention to the the direction of the switch in the images below.  Having the switch rotated by 90 degrees from the way it is in the image will result in a non-working switch**

Include your switch in the circuit/schematic below:

<figure>
  <p><img src="CURRENT/switch_input.png" width="35%"/>
  <figcaption>Switch as Input</figcaption>
</figure>

Then create a new file and paste the code into it below:

<pre class="prettyprint linenums lang-python">
import RPi.GPIO as GPIO  #import library to use input/output pins
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
input_pin = 5
GPIO.setup(input_pin,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
while True:
    if GPIO.input(input_pin)==1:
        print("Pushed")
    time.sleep(0.05)
</pre>

Some of these pieces should start looking familiar, but others are new...let's go over the chunks again:


The first four lines are like from earlier...import libraries and set some basic utility things up. You'll usually always use these four lines.


<pre class="prettyprint linenums lang-python">
import RPi.GPIO as GPIO  #import library to use input/output pins
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
</pre>

The next two lines set up a GPIO pin as an input.  We create a variable `input_pin` and set it to `5` and then use that second line to establish that the pin is an input.

<pre class="prettyprint linenums lang-python">
input_pin = 5
GPIO.setup(input_pin,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
</pre>

The last part takes some explaining.  A <codep>while True</codep> loop is a way to get a block of code to run forever. Normally a <codep>while</codep> loop runs as long as its condition that it is checking is <codep>True</codep>. Since <codep>True</codep> is always <codep>True</codep> this loop will run forever (until we stop it with a Control-C).

So the loop doesn't run 1000's of times per second we put a `time.sleep` command to pause the code for 0.05 seconds each time through, keeping our loop running no faster than 20 times per second.  

Finally each time through the loop we check to see if our switch is pushed. We do that by checking the value of the switch with the command <codep>GPIO.input(input_pin)</codep>.  This provides a value that could be stored in a variable if we wanted, but we check if it is <codep>1</codep> in value and if it is, we print <codep>"Pushed"</codep>.


<pre class="prettyprint linenums lang-python">
while True:
    if GPIO.input(input_pin)==1:
        print("Pushed")
    time.sleep(0.05)
</pre>


<framedtext>Goals: In Lab 04 we will continue with what you started in Lab03 (so finish that lab first) and </framedtext>

<section>State Machines and Double-Clicking</section>

We're going to now make a simpler music player that uses only one button (the button connected to GPIO 12):

* Single Click corresponds to Pause/Unpause on a song
* Double Click on a button corresponds to song switch (similar to before)

The functionality is shown in the video below:
<center>
<a href="https://www.youtube.com/watch?v=p7O1H-bzuhY&feature=em-upload_owner" target="_blank">VIDEO</a>
</center>

Some pre-lab thoughts are included in this video:
<center>
<iframe width="560" height="315" src="https://www.youtube.com/embed/cJMeNSvQh0U" frameborder="0" allowfullscreen></iframe>
</center>

<section>Flow Diagrams and State Machines</section>

The code you need for this lab is going to take in all that you've learned so far.  Whenever you start coding out a solution to a problem, often times the beginning is the worst since the problem can seem just so massive that you don't know where to start.  What I usually do is try and sketch out an idea of my control flow...what paths will my code take as it runs...What ends up happening might not 100% match what you initially sketched out but at least this helps you get started. Here's the flow diagram I quickly sketched out when I was coming up with this lab.

An important concept that can really help with handling problems is the idea of a state machine. To understand what a state machine is, we first need to understand what a state machine isn't...and that is a stateless machine. (note when we say "machine" we mean any sort of object (piece of code, robot, actual machine, etc...)

If you were to have a machine that always takes in a numerical input and immediately prints out three times that number regardless of what has happened in the past, we'd call this a "stateless" system. Basically the way it responds is based solely on its inputs and nothing else.  For example...here's a stateless function in Python:
```
def slm(x):
    return 3*x
```

No matter how many times you call the function `slm` it will always do exactly the same operation.  It lives in the moment with no concern for the past.  If you were to do three simultaneous calls on `slm` of: `slm(2)`, `slm(2)`, `slm(2)`, each time you'd get back `6`. 

A state machine, in contrast, could be thought of as a machine that not only responds to inputs, but also takes previous inputs into consideration when formulating its output.  The way these previous inputs influence the system's response manifests itself in the form of a "state" as in state of mind...as in New York State of Mind by Nas.

In order to accomplish such a functionality, state machines need to be able to remember...they need to have memory and this memory generally takes the form of variables.  The following is a state machine:

```
seen_a_two = False
def sm(x):
    global seen_a_two #give sm permission to change this variable
    if seen_a_two:
        val= "I'm done"
    else:
        val=3*x
    if x == 2:
        seen_a_two = True
    return val
```

Now if you were to run this function three times with the same input of `2` (just like before) what you'd get is: `6`, `"I'm done"`, `"I'm done"`.  

So in this situation the same input (`2`) yielded different outputs because the **state** of the system was different different times.


This is a stupid example, but should highlight an important idea that we can have code that responds differently to identical inputs based on what has been seen before, and as a result make decisions based off of that.

<div class="note">Another state machine example is a human eating food. We put food in our mouth and eat, and then put food in our mouth and eat...but eventually our "state" changes and even if we were to put food into our mouth we might not want to eat any more or might throw up.  Intelligence/Life can in some sense be characterized by the presence of state machines. A rock will always do the same thing when you yell at it...but a dog or a human will eventually tire of your anger and walk away or yell back or something.  
</div>


<subsection>Flow Diagrams</subsection>

A good way to start thinking about state machines is by sketching out how we want to respond inputs and putting it down in a flow diagram.  An example one is shown below. Different states of the system are in the blue boxes and diffrent decision points are in the diamond shapes.  See if you can map the decisions and states and how they are implemented in vivo in the code below.
<center>
<img src="CURRENT/state_flow_1.png" width=200/>
</center>

```
def system():
    state = start
    while True:
        action = action() #get action each time through loop
        if state == start:
            if action == 'A' or action == 'C':
                state = state1
            else: #if action is 'B'
                state = start
        elif state == state1:
            if action == 'A':
                state = start
            elif action=='B':
                state = state2
            else: #action is C
                state = state1
        else: #state is state2
            state = start #immeidately go from state2 to start
```


<section>Waiting and Timeouts</section>

For assessing double clicks you're going to need to implement a timeout in conjunction with your listener.  To do this we need two things...a way to continuously listen for actions and a way to keep track of how long code has been running.  For the former we can use waiting loops and for the latter we can use timeouts and the `time.time()` method. 

<subsection>Waiting</subsection>

Often times in code you need to just hang out and wait for a user input. This structure is known by many things, depending on the context, but we can just call it a "waiting loop" in our class.  If you want to pause your code until something happens you can do the following:
```
print('Waiting for Button press')
while GPIO.input(pin_number) != 0:
    pass
print('Button pressed!')
```
In this small snippet of code, imagine that `pin_number` references a push button switch in a **pull-up** configuration. Normally this switch would be outputting high (1).  Therefore this while loop will continually loop (and do nothing) as long as `GPIO.input(pin_number)!=0` returns `True`. When the button is pushed...this comparison will fail and the `while` loop will be exited! How often will it check the pin?  Very often.  Probably ever 100 micro seconds or so....which in human time is really fast (in computers this is actually really slow, but that's ok.)

<subsection>Timeouts</subsection>

When you call `time.time()`, it will return the number of seconds that have elapsed since <a href="https://en.wikipedia.org/wiki/Unix_time" target="_blank">Midnight on January 1st, 1970</a>.  Why is this useful?  Well, while we rarely need the actual value returned by `time.time()` using multiple calls on it can be used to find the amount of time it took to run a piece of code. For example:
```
start_time = time.time()
for x in range(500):
    print('EECS is the best field of study.')
stop_time = time.time()
print(stop_time - start_time)
```
This code will print the amount of time it takes for that `for` loop to run 500 times.  This is pretty cool. Very, very rarely do we use a single call on `time.time()`. Instead we usually use the differential of multiple calls to figure out durations.  For example if you started doing a task at 1e6 seconds after the start of January 1, 2016 and finished that task 1.01e6 seconds after the start of January 1,2016, you can use these two numbers to realize that it took you 0.01e6 seconds (10,000 seconds) to do the task.

Now that we can time things, let's imagine we wanted to know if an event happened within a certain amount of time from the start of running our code.  We can repeatedly listen for that event until too much time has passed.  If 

```
event_in_time = False
timeout = 0.5 #seconds
start_time = time.time()
while time.time() - start_time < timeout:
    input = listen_for_event()
    if input:
        event_in_time = True
print(event_in_time)
```

If we'd like to furter improve this code we could have it exit the loop as soon as the event is observed rather than keep running even though the event already happened. This can be done with the `break` command

```
event_in_time = False
timeout = 0.5 #seconds
start_time = time.time()
while time.time() - start_time < timeout:
    input = listen_for_event()
    if input:
        event_in_time = True
        break
print(event_in_time)
```

The piece of code above IS EXTREMELY COMMON AND SUPER USEFUL. It is basically used in almost all communication services...any time you are listening for a signal or input or anything, something very similar to the piece of code above is running (this prevents you for listening forever.)

We do timeouts all the time as humans. If our friend said they were going to meet us at the roller skating rink at 9pm we'd probably wait for five minutes...constantly running a while loop in our head and checking our phone and checking to see if he/she shows up.  If after five minutes they don't ,then we "time out" and leave.  

So you need to do that for discerning single from double clicks.  

Use the flow diagram below as a starting point.


<center>
<img src="CURRENT/double_click_state_flow.png" width=400/>
</center>

We're going to encapsulate this logic within a function called `click_getter`  This function should be able to fit within the following skeleton code and return a value either `None`, `1`, or `2`.  The code will then do the following based on these three values:

* `None`: Do nothing
* `1`: Pause or Unpause a song
* `2`: Skip to the next song and start playing it

The code skeleton found <a href="CURRENT/lab03.zip">here</a> should be used to develop your function.  READ THROUGH THIS CODE A BIT BEFORE YOU DIVE IN!  IN PARTICULAR:

* `click_getter()` should base its double click listening timeout on the global variable `TIMEOUT` defined at the top of the file!

Your `click_getter` function should be able to pass the tests below:

<question pythoncode>
csq_code_pre = r'''import time
TIMEOUT =0.01

##Fake GPIO class:
eg1 = [True,True,False,True,False,True,True]
eg2 = [True,True,True,True,True,True,True]
eg3 = [False,True,True,True,True]
eg4 = [False,False,True,False,True]

class Test:
    def __init__(self, history):
        self.history = history
        self.index=0
    def input(self,pin):
        if pin != 12:
            return False
        new_val = self.history[self.index]
        self.index +=1
        self.index%=len(self.history)
        return new_val
'''

csq_initial = '''def click_getter():
    pass
'''

csq_soln="""def click_getter():
    input = GPIO.input(12)
    state=None
    if input == 0:
        while GPIO.input(12)==0:
            pass #wait
        state=1
        start_time = time.time()
        while time.time()-start_time <TIMEOUT:
            input = GPIO.input(12)
            if input==0:
                state=2
                break
        if state==2:
            while GPIO.input(12)==0:
                pass
    return state

"""

csq_nsubmits = float(40)
csq_tests = [{'code':'GPIO = Test(eg1)\nans =click_getter()'},
{'code':'GPIO = Test(eg2)\nans =click_getter()'},
{'code':'GPIO = Test(eg3)\nans =click_getter()'},
{'code':'GPIO = Test(eg4)\nans =click_getter()'}]
</question>

Once it is working, add it into the `lab03b.py` code and show it to a staff member!  Finally, upload your entire file below for documentation/review!

<question fileupload>
csq_check_function = lambda x,y:True
</question>

<div class="critical">Did you finish early?  No, you didn't.  If you find yourself all done, you need to now add in some of the following functionality:
<ul>
    <li><strong>Volume Control:</strong> We got rid of software-based volume control in this lab, but now you need to go back and add it in. Come up with a scheme that will allow you to increase and/or decrease volume using the single button and additional gestures/time sequences...perhaps a single long hold, starts increasing the volume in 10% increments at 1 second intervals and a single click followed by a quick long-hold, starts decreasing the volume in 10% increments. It is up to you...if you'd like you can add up to one more switch if it helps.</li>
    <li><strong>Forward and Backward Song Skip:</strong>  So far we can only skip through songs in one direction...try to do both directions now. You can add an additional switch if you'd like!</li>
</ul>