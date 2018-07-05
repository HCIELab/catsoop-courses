<section>Hardware</section>

The Raspberry Pi has a number of external interfaces that we can use to generate inputs and outputs. Inputs can be keyboards, but they can also be more "bare-bones." Among these inputs, the Raspberry Pi has a number of <b>General Purpose Input Output (GPIO) Pins</b> that we can use to obtain simple inputs and outputs. By "simple" we mean digital, and by digital we mean Yes/No On/Off, etc... We can do a lot with these. An overview of the workstation we'll be using is shown below: You should have a near identical unit in front of you as you read this.

<figure>
  <p><img src="CURRENT/overall_explain.jpg" style="width:6in" />
  <figcaption>Our standard Raspberry Pi Workstation.</figcaption>
</figure>

<subsection>Breadboard</subsection>


Most of our circuit building will take place on what we call a <a href="http://en.wikipedia.org/wiki/breadboard" taret="_blank">"breadboard</a>.  The breadboard is a convenient prototyping device which allows us to quickly build up circuits rather than have to rely on twisting component leads together.

<figure>
  <p><img src="CURRENT/breadboard.jpg" style="width:6in" />
  <figcaption>A standard breadboard.</figcaption>
</figure>


The breadboard can be a little hard to understand at first, but it really doesn't need to be. We'll be using the breadboard a lot, so it is good to learn how it operates. Each hole in the breadboard goes down into a metal grabber thing. The grabber part allows electrical parts to be stuck in and held in place.  Each thing often has several grabbers associated with it so two or more electrical parts can be held onto the same surface. The metal aspect of the grabber allows those parts to be electrically connected to one another. (Remember metal is a conductor which means charge can flow easily over it...two components connected by a piece of metal are electrically connected). Often regions of continuous conductor are called a "node".  The way the metal is wired up in the breadboard is shown in the Figure below. The green boxes show example sets of holes that are connected together.

<figure>
  <p><img src="CURRENT/bb_explain_small.jpg" style="width:6in" />
  <figcaption>Breadboard Construction.</figcaption>
</figure>


Answer the questions about a few breadboard connections below.
<figure>
  <p><img src="CURRENT/breadboard_quiz.jpg" style="width:4in" />
  <figcaption>Small Breadboard Quiz</figcaption>
</figure>

Enter your answers as capital letters separated by commas only (if the correct answer is `B` then enter '`B`' below.. If there are more than one correct node enter all...so that if the correct answer is `B` and `L` then enter: '`B,L`'.  Enter `None` if there are no other connected nodes.

<python>
def breadboard_checker(x,y):
    good = True
    for q in x:
        if q not in y and q != ' ':
            good = False
    for q in y:
        if q not in x and q!= ' ':
            good = False
    return good
</python>

<question smallbox>
csq_hint = '''Pay attention to how the rows are connected.\nPay attention to gap in the middle of the board.'''
csq_prompt = 'What other nodes are connected to Node A?'
csq_soln = 'B,J'
csq_check_function=breadboard_checker
</question>

<question smallbox>
csq_prompt = 'What other nodes are connected to Node D?'
csq_hint = '''Pay attention to how the rows are connected.\nPay attention to gap in the middle of the board.'''
csq_soln = 'C'
csq_check_function=breadboard_checker
</question>

<question smallbox>
csq_prompt = 'What other nodes are connected to Node H?'
csq_soln = 'None'
csq_check_function=breadboard_checker
</question>

<question smallbox>
csq_prompt = 'What other nodes are connected to Node K?'
csq_soln = 'M'
csq_check_function=breadboard_checker
</question>

<question smallbox>
csq_prompt = 'What other nodes are connected to Node F?'
csq_soln = 'G'
csq_check_function=breadboard_checker
</question>

<note>Sometimes we'll call the really long nodes "rails" or "busses" depending on the situation. It doesn't change what they are!!</note>.

<note>Some of you may have slightly different numbers of nodes in your breadboard so the answer below only needs to be approximate</note>
<question pythonic>
csq_prompt="How many total electrical nodes are located on your breadboard (counting the long ones on both sides?)"
csq_soln = 132
csq_check_function = is_close(0.05)
</question>

<subsection>Breakout Board</subsection>
The Pi is connected to the outside world through a ribbon cable that then connects to a board known as a "Breakout".  The Breakout, shown in the image below, gives us nice, clean, readable access to all the Pi's pins.

<figure>
  <p><img src="CURRENT/breakout.jpg" style="width:3in" />
  <figcaption>The Breakout</figcaption>
</figure>

In the photo above, two wires are used to connect the `3V3` pin and the `GND` pin of the Raspberry Pi to the + left rail and the - left rail of the breadboards.  The `3V3` pin is positive voltage (of 3.3V). The `GND` is. Very often it is a good idea to use the really long nodes on both sides of the breadboard as a way to distribute power and ground across the breadboard so you don't need to use really long wires all the time.

**When we draw out the breakoutboard in this lab and later labs we'll often just represent it as a gray box.**

<section>Components</section>
There are five circuit elements that we'll work with now (and more later).  They're each discussed briefly below.

<subsubsection>Voltage</subsubsection>

<figure>
  <p><img src="CURRENT/3V3.png" style="width:0.5in" />
  <figcaption>The Voltage Symbol</figcaption>
</figure>


This symbol represents a connection to the positive voltage of 3.3V.  It is accessible via the `3V3` pin on your breakout board.  In conjunction with the `GND` shown next, provide the power for most of our work and experiments. Since we'll often need to make many connections to 3.3V it is often a good idea to distribute this voltage out using the "+" busses on both sides of the breadboard.
<subsubsection>Ground</subsubsection>

<figure>
  <p><img src="CURRENT/GND.png" style="width:0.5in" />
  <figcaption>The Ground (0V) Symbol</figcaption>
</figure>

This symbol represents a connection to the ground voltage of 0V.  It is accessible vias the `GND` pin on your breakout board. In conjunction with the `3V3` pin (which provides +3.3V), these pins provide most of the power for our work and experiments.  Since we'll often be making many connections to ground it is often a good idea to distribute this voltage across the breadboard by using the "-" busses on both sides of the board.

<subsubsection>Resistor</subsubsection>
<figure>
  <p><img src="CURRENT/resistor.png" style="width:0.5in" />
  <figcaption>The Resistor Symbol</figcaption>
</figure>

This is the symbol for an electrical resistor, which is a device that resists the flow of electricity. In real life, resistors are the small tan cylinders with different colors on them. The colors tell us what value they are (in Ohms). Don't worry about memorizing that color code. We'll write python code to figure it out for us eventually.  **It doesn't matter what direction you plug a resistor in!**  For today, and many days, staff will help you with the resistor colors/values.


<figure>
  <p><img src="CURRENT/real_life_resistor.jpg" style="width:40%" />
  <figcaption>The Wild Resistor</figcaption>
</figure>

<subsubsection>LED</subsubsection>

<figure>
  <p><img src="CURRENT/LED_schematic.png" style="width:1.0in" />
  <figcaption>The LED Symbol</figcaption>
</figure>

Light-Emitting Diodes (<a target="_blank" href="http://en.wikipedia.org/wiki/Light-emitting_diode">LEDs</a>) are small do devices that do basically what their name implies: emit light. LEDs can be many different colors as well as emit radiation in the ultraviolet and infrared spectrum.  The schematic symbol for an LED is a triangle with a line next to it. The "D" part of LED stands for "diode" (it is a light-emitting diode), and diodes have to be hooked up in a certain direction like shown in the figure below:

<figure>
  <p><img src="CURRENT/LED_hookup.png" style="width:4in" />
  <figcaption>The hooking up of an LED</figcaption>
</figure>

Additionally, LEDs *generally* need to be hooked up <i>in series</i> with a resistor when being connected to a voltage source like shown below.

<figure>
  <p><img src="CURRENT/LED_circuit.png" style="width:1in" />
  <figcaption>A proper and healthy LED circuit</figcaption>
</figure>

<subsubsection>Switch</subsubsection>
The final electrical component we'll be talking about is the switch. Its schematic symbol is the following:

<figure>
  <p><img src="CURRENT/switch.png" width="15%" />
  <figcaption>A switch</figcaption>
</figure>

There are many, many types of switches, and you'll gain some experience with several of them. What they all do, however is selectively control electricity.  For today's lab we'll be using what are called "Normally Open Momentary" switches.  This means that when left untouched, the two terminals of the switch are disconnected, but when you press on the button, the two terminals connect.  In real life our switches look like what is shown in the figure below, where we've also provided an image of the switch in the context of the breadboard.

<figure>
  <p><img src="CURRENT/switch_hookups.jpg" width="45%" />
  <figcaption>The switch we'll be using today</figcaption>
</figure>

You can plug your switch into the breadboard as shown above.

<note>Pay attention to the the direction of the switch in the images below.  Having the switch rotated by 90 degrees from the way it is in the image will result in a non-working switch</note>

<section>Let's Build</section>

OK let's build some stuff.  First off, let's create a simple LED circuit with a resistor.  Pick an LED from up front (any color) and then pick a $330 \Omega$ (ask for help if you can't find label) resistor.  Use these parts (and some wires to build the following:

<figure>
  <p><img src="CURRENT/circ_build1.jpg" style="width:1in" />
  <figcaption>The first circuit to build</figcaption>
</figure>


When it is glowing and you're happy with the state of things, replace the 330 Ohm resistor with a 5Kilo-Ohm (5K) resistor...(ask for help if you can't find it). What do you observe?

<figure>
  <p><img src="CURRENT/circ_build1a.jpg" style="width:1in" />
  <figcaption>The first circuit to build (with modification)</figcaption>
</figure>

Now replace your 5K resistor with the original 330 Ohm one.  Make D1 a red LED and add a second LED D2  **in paralallel** to the first.  What do you observe? Replace LED D1 with one of the same color (red).  What do you observe?

<figure>
  <p><img src="CURRENT/circ_build2.jpg" style="width:1.5in" />
  <figcaption>Our new circuit (with multiple LEDs)</figcaption>
</figure>

Different color LEDs require different voltages across them to operate, and it is often very difficult (or impossible) to run two LEDs of different types when in parallel.  A more correct way to do it is to add a second isolated path with its own resistor.  Build the circuit below where D1 is a red LED and D2 is a white LED.

<figure>
  <p><img src="CURRENT/circ_build3.jpg" style="width:2in" />
  <figcaption>Our new circuit (with multiple isolated LEDs)</figcaption>
</figure>

Mkay, let's add in some switches.  Build the circuit below (with whatever color LED you want).  What should this circuit do?  What does this circuit do after you build it.


<figure>
  <p><img src="CURRENT/circ_build4.jpg" style="width:1in" />
  <figcaption>LEDs and switches</figcaption>
</figure>


All right. With two switches, build a circuit that glows the LED only when **BOTH** switches are turned on (pushed).  Show it to a staff member when it is working:


<figure>
  <p><img src="CURRENT/circ_build5.jpg" style="width:1in" />
  <figcaption>Build it</figcaption>
</figure>

<section>Audio Amplifier</section>

OK now that we've got some basic circuits out of the way, we're going to build an audio amplifier. Shown below is the schematic of the amplifier we're constructing.  We don't expect you to know how to build this off the bat, so first we're going to discuss each of the new parts that are in it.  

<figure>
  <p><img src="CURRENT/audio_amp_schematic.png" width=800>
  <figcaption>Audio Amplifier</figcaption>
</figure>


<subsubsection>TRS Connector</subsubsection>
First up on the left side of the schematic above is a symbol that should look familiar to you millenials. It is a **T**ip **R**ing **S**leeve connector, which is usually abbreviated as "TRS" connector.  This is the same piece of equipment which you usually use to get music from your phone into your headphones. It is comprised of three conductors separated by two plastic insulators. The conductor regions make pressure connections inside the phone with tiny pins that provide the left audio voltage, the right audio voltage, and a ground connection (very similar to a key in a lock). Usually three wires come from the TRS connector to your earbuds: One wire (left or right) and the ground wire go to one earbud, and the other wire (right or left) and the ground wire go to your other earbud... We're going to merge the left and right wires (orange and red) wires together here. The result is that our amplifier will be mono rather than stereo. If you want to incoporate a stereo amp into your final project later on that's definitely a possibility.
<figure>
  <p><img src="CURRENT/trs_connector.png" width=500>
  <figcaption>The Tip-Ring-Sleeve (TRS) connector</figcaption>
</figure>


<subsubsection>Potentiometer</subsubsection>
The next part of the schematic is this device, which looks like a resistor in a gray box with an arrow pointing to it.  This similarity is well-justified
<figure>
  <p><img src="CURRENT/pot_schematic.png" width=400>
  <figcaption>The potentiometer</figcaption>
</figure>

This part is known as a potentiometer (or "pot"). It is basically a variable resistor network, which we use as a variable voltage divider circuit (you'll start doing the math for voltage dividers in HW03!), and what it does is act as a volume control. We'll analyze the math behind it in Homework 04.  In real life for this lab it looks like this:

<figure>
  <p><img src="CURRENT/pot_real.jpg" width=300>
  <figcaption>The potentiometer in real life</figcaption>
</figure>


and that links to what is drawn in the schematic with the following:

<figure>
  <p><img src="CURRENT/pot_link.jpg" width=300>
  <figcaption>The potentiometer in real life</figcaption>
</figure>


The legs on the potentiometer are not randomly assigned! (The middle arrow leg in the schematic coresponds to the middle leg in real life, while the two side legs can be flip-flopped as needed). So as you build you circuit please pay attention to which one you hooking up to what part.

<subsubsection>Amplifier Chip</subsubsection>
The next device you see in the schematic (going left to right) is the triangle-shaped thing which is an audio amplifier.  The audio amp that we'll be using looks like the following in real life:

<figure>
  <p><img src="CURRENT/lm386n1_real.jpg" width=200>
  <figcaption>Audio Amplifier Chip</figcaption>
</figure>


The audio amplifier we're using is known as an LM386-N1 and it exists in an 8-Pin DIP.  The "8-Pin" part comes from the fact that it has 8 legs. The DIP part comes from the term <b>D</b>ual <b>I</b>nline <b>P</b>ackage. The pins on a DIP type device start in the lower left and go counter-clockwise:

<figure>
  <p><img src="CURRENT/lm386_pinnout.png" width=250>
  <figcaption>LM386 Pinout</figcaption>
</figure>

It is useful to be able to read the text on the chip since the LM386 is only one of hundreds of thousands of types of DIPS that all look nearly identical except for number of pins and text on them.  The diagram below explains a bit more about how to read DIP chips:

<figure>
  <p><img src="CURRENT/lm386_deep_explain.png" width=600>
  <figcaption>A more detailed explanation of the DIP labeling</figcaption>
</figure>


To use the LM386 (or any DIP you'll want to place it across midline gap so that each of the package's eight legs have their own individual node on the breadboard. On the schematic for the audio amplifier the pin numbers are labeled.  So for, example, Pin 6 goes to 3.3V.

<subsubsection>Capacitor</subsubsection>
<python>
'''
There are two instances of this symbol in the schematic. Some of them are the symbol with two parallel lines that has a "+" marked on one side of it. This is what we call a "polarized capacitor" or an "Electrolytic Capacitor".  

We haven't encountered <a href="https://en.wikipedia.org/wiki/Capacitor" target="_blank">capacitors</a> yet, but they are usually used for energy storage or for filtering (both uses are happening in this circuit). 

<center>
<img src="CURRENT/capacitor_basic.png" width=70>
</center>

This first type of capacitor is the <a href="https://en.wikipedia.org/wiki/Electrolytic_capacitor" target="_blank">Electrolytic Capacitor</a> and must be connected in the direction indicated by the "+" symbol.  In real life they look like in the image shown below, which explains how to read and figure out which lead is which on them: For this circuit, the exact value of the capacitor doesn't matter...so long as you use one of the polarized capacitors where it says to.

 
<center>
<img src="CURRENT/capacitor_explain.jpg" width=500>
</center>
'''
</python>

The capacitors we use in this class are non-polar capacitors, which means you can hook them up in either direction:

<figure>
  <p><img src="CURRENT/non-polar-cap.jpg" width=500>
  <figcaption>The non-polar capacitor</figcaption>
</figure>

We'll be using one capacitor (C3) as a bypass capacitor, the purpose of which is to minimize power supply noise.  It sort of acts like a power supply water tower, absorbing spikes in power and providing sufficient voltage when there are power dips (which happen all the time). The result is a constant "water pressure" of voltage for the circuit so there aren't any noise problems. You'll need to place it close to your LM386-N1 chip like shown below:

<figure>
  <p><img src="CURRENT/non-polar-hookup.jpg" width=500>
  <figcaption>The bypass capacitor</figcaption>
</figure>


Capacitor C1 and C2 are used to allow only the audio signal through.

<h3>Speaker</h3>
The speaker is where noise comes out. It is an eletro-audio transducer, converting a varying electrical field (linked to the varying voltage) to a varying magnetic field which then causes movement of a mechanical diaphram which pushes and pulls air back and forth causing sound waves to form.  Our speaker looks like the following in the schematic and in real life, respectively:

<figure>
  <p><img src="CURRENT/speaker.jpg" width=500>
  <figcaption>The speaker</figcaption>
</figure>


<h3>System Overview</h3>
So again, now that we've reviewed each schematic component, let's take a look at the overall schematic again:

<figure>
  <p><img src="CURRENT/audio_amp_schematic.png" width=800>
  <figcaption>The audio amplifier schematic overall</figcaption>
</figure>


You should be able to see a rought left-to-right flow of signal. On the left side, audio from the Raspberry Pi comes in through the TRS connector, before being adjusted using the potentiometer.  This adjusted signal is then fed into the audio amplifier chip (NJM2113), and then being used to drive a speaker that provides sound.  This step-by-step discussion of the amplifier emphasizes the "stages" of the device.  The high level stages of the whole amplifier are shown below:

<figure>
  <p><img src="CURRENT/amp_stages.png" width=800>
  <figcaption>The stages of the audio amplifier</figcaption>
</figure>

<section>Gain</section>
When you build this circuit you'll be able to produce music at varying volume by turning the potentiometer.  When you vary the volume of this system you are varying the **Gain** of the amplifer.  Gain of an amplifier is usually described by the variable $A$.  The total gain of an amplifier is $A_{tot}$. If our input music signal is a voltage $V_{in}$ and our amplified output signal is $V{out}$, we can relate the two of them by using the gain such that:
$$
V_{out} = A_vV_{in}
$$

Gains can often be sketched out as being represented by triangles (one triangle for each stage). The total gain of our amplifier comes from the series accumulation of several gain stages, in particular the gain of the potentiometer stage (which varies from $0$ to $1$ based on the angle that you've turned it to), and the gain of the NJM2113 chip which is ideally fixed at $20$.  When gains are in series with one another their total gain is their product as shown below. For example if you had three gain stages in series, $A_1$, $A_2$, and $A_3$, the total gain of the system would be their product $A_1A_2A_3$:

<figure>
  <p><img src="CURRENT/series_gains.png" width=700>
  <figcaption>Signal Gains in Series</figcaption>
</figure>

<python>
"""
<question pythonic>
csq_prompt="Using what we just learned and the sytsem diagram above, what is the lower bound of gain in our overall amplifier circuit?"
csq_soln = 0
csq_check_function = lambda x,y: x==y
</question>

<question pythonic>
csq_prompt="Using what we just learned and the sytsem diagram above, what is the upper bound of gain in our overall amplifier circuit?"
csq_soln = 20
csq_check_function = is_close(0.1)
</question>
"""
</python>

<section>Build It!</section>

OK time to build your amplifier circuit. Follow the schematic as best you can!

* Keep your wires short. Doing this will minimze noise! (you may not believe me but it will)

When done, show your system to a staff member and they will test it. 

<section>Audio Playing</section>


<pre class="prettyprint linenums lang-python">
import time
import pygame

try:
    pygame.mixer.init()
    pygame.mixer.music.load('/home/pi/oeop_files/audio/song1.mp3')
    pygame.mixer.music.play()
    time.sleep(6)
    pygame.mixer.music.stop()
    print('Playing')
except KeyboardInterrupt:
    pygame.mixer.music.stop()
    print('Stopped!')
</pre>


<section>Final Assignment</section>

If you're all done, there are two final assignments we'd like you to do. They are:

* Build a System that plays audio only when a switch is pressed (and held down). There are multiple ways to do this!
* Build a system that selects between two audio sources...so you can play audio source 1 when button 1 is pressed and audio source 2 when button 2 is pressed. There are also multiple ways to do this.







<python>
'''

Where did that sound come from? Well when you press that button, it runs the following code:

```
import time
import pygame

try:
    pygame.mixer.init()
    pygame.mixer.music.load('/home/pi/mostec17/audio/freq_sweep.mp3')
    pygame.mixer.music.play()

    time.sleep(6)
    pygame.mixer.music.stop()
    print('All Good')
except:
    print('Comm Failure')
```

This code is based on the pygame library and, is what you'll be focussing on for the rest of the lab! This example is pretty simple, but what you'll need to do now is pretty complex. 

The first part of the code should look pretty familiar from Lab 02.  We are importing and messing with a new library, however called the `pygame` package.  This is a very versatile Python library intended for developing games.  We'll be using it to play music here.  We can use `pygame` to play music using four commands (where appropriate). Two of the commands are already implemented for you:
```
pygame.mixer.init()
```
sets up a "mixer" which is a Python object that allows music to be played.
```
pygame.mixer.music.load(song_name)
```
loads the mixer with a song file contained in the variable `song_name`.  As of right now the song is simply a frequency sweep mp3 file. Feel free to download and use your own songs. There is a video of a fully-functioning system at the end of the lab has some TSwift and others. Pygame really needs the file to be in mp3 so only get those. While downloading music files is not a good thing to do, you're all millenials, so I'm sure you know where to download files easily. If you don't, <a href="http://www.mp3juices.cc" target="_blank">this site</a> works pretty well. Pay attention to where you save your downloaded files, and feel free to move them and rename them more reasonable names (than what they are usually default named) to make your life easier when getting them to work with Python.

When you want to play a song you need to run:
```
pygame.mixer.music.play()
```
which will start the song playing (and it runs in the background). When you want to stop a song, you'll need to run:
```
pygame.mixer.music.stop()
```
which stops the song.

There are a lot more commands, and one of the things we want you to get experience is in reading the documentation on libraries.  For the pygame music package, you can go here: <a href="http://www.pygame.org/docs/ref/music.html" target="_blank">pygame documentation</a>. You will need to read through this documentation and experiment with these commands and function calls to complete this lab. In week 3, we'll be writing a game using the Pygame package, which is a really flexible Python-based package so the sooner you get used to looking things up for this library the better.

That's it for this lab.  If you can basically play music out of your system, you're good to go!
'''
</python>
