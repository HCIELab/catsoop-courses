<python>
cs_scripts += '<script type="text/javascript" src="COURSE/scripts/scrollspy_builder.js"></script>'
types = ['num','int','float','bool','noneType']
numeric_check = lambda x,y: type(x) == type(y) and abs(x-y)<1e-6
#submitted,solution
def list_check(x,y):
    return (len(x)==len(y)) and False not in [q[0]==q[1] for q in zip(x,y)]

def is_close(closeness):
    def close(x,y):
        return  abs((x-y)*1.0/y)<closeness
    return close

csq_nsubmits = 10
</python>
<center>
<a href="https://www.youtube.com/watch?v=apN0AXjJxQE" target="_blank">Music for Exercise</a>
</center>

<section>Clipping</section>

One of the nice things about modeling the world is that we can model real life (physical phenomena) with equations, however often times nice "pretty" equations only exist in certain ranges. Let's take falling, for example. If you drop an object off of a very tall building, its velocity as a function of time could be described with the following equation:
$$
v(t) = at
$$ 

where $a$ is acceleration (in meters$\cdot$s$^{-2}$) and $t$ is time (in seconds).  So on earth, $a = g = 9.81\text{m}\cdot\text{s}^{-2}$ and therefore after ten seconds, using only this equation, any falling object would have a velocity of what (in meters per second)?

<question pythonic>
csq_soln = 98.1
csq_check_function = is_close(0.01)
</question>

In reality this isn't necessarily the case.  On Earth and any place with an atmosphere you'll have to deal with air resistance, and the net effect is that the faster an object moves, the more resistance it faces from air. Eventually the force on the falling object from air will cancel out the force on the falling object from gravity.  Because acceleration $a$ is directly proportional to net force ($F=ma$), the object will cease accelerating and reach what is termed a <a href="http://en.wikipedia.org/wiki/Terminal_velocity" target="_blank">terminal velocity</a>, a velocity at which the object will continue falling at.

Write a Python function `velocity_with_term`  that takes in three arguments:

* <codep>t</codep>: time
* <codep>a</codep>: acceleration (maybe we're not on Earth)
* <codep>V</codep>: terminal velocity

And returns the velocity of the object (assuming acceleration is constant, and there is infinite room for falling...ie the object never hits the ground).

You can assume a discontinuous velocity profile similar to that shown below:

<figure>
  <p><img src="CURRENT/velocity.png" width=400 />
  <figcaption>A rough plot of how terminal velocity looks like over time.</figcaption>
</figure>

<question pythoncode>
mess = tuple(cs_random.randint(1,900)*0.01 if x in [1,4,7,10] else cs_random.randint(0,500) for x in range(12))
csq_initial = '''def velocity_with_term(t,a,V):
    pass
'''
csq_soln = '''def velocity_with_term(t,a,V):
    possible_velocity = t*a
    if possible_velocity > V:
        return V
    else:
        return possible_velocity
'''
csq_tests = [
    {'code':'ans = velocity_with_term(3,9.81,40)'},
    {'code':'ans = velocity_with_term(5,9.81,40)'},
    {'code':'ans = velocity_with_term(%s,%s,%s)' %mess[0:3]},
    {'code':'ans = velocity_with_term(%s,%s,%s)' %mess[3:6]},
    {'code':'ans = velocity_with_term(%s,%s,%s)' %mess[6:9]},
    {'code':'ans = velocity_with_term(%s,%s,%s)' %mess[9:12]},
    ]
</question> 
