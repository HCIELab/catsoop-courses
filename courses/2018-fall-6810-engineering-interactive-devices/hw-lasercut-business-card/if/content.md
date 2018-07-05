<python>
cs_scripts += '<script type="text/javascript" src="COURSE/scripts/scrollspy_builder.js"></script>'
</python>

<center>
<a href="https://www.youtube.com/watch?v=xVPzd2IPvR0" target="_blank">IF</a>
</center>

Below is a transcript of a session with the Python shell.  Provide the type and value
of the expressions being evaluated.  If evaluating the expression would cause an error, write <codep>error</codep> in the box.  If the value of the expression is a function, write <codep>function</codep> in the box.  Assume the following definitions have been made:

<pre class="prettyprint linenums lang-python">
def a(x, y, z):
     if x:
         return y
     else:
        return z

def b(y,z):
    return a(y>z, y, z)
</pre>

<pre class="prettyprint lang-python">
>>> a(False, 2, 3)
</pre>
<question pythonliteral>csq_soln=3</question>

<pre class="prettyprint lang-python">
>>> b(3,2)
</pre>
<question pythonliteral>csq_soln=3</question>

<pre class="prettyprint lang-python">
>>> a(7&gt;4, a, b)
</pre>

<question smallbox>csq_soln='function'</question>
