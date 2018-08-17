<python>
types = ['num','int','float','bool','noneType']
numeric_check = lambda x,y: type(x) == type(y) and abs(x-y)<1e-6

tutor.init_random()
csq_nsubmits = 10
</python>

<center>
<a href="https://www.youtube.com/watch?v=0YuaZcylk_o" target="_blank">Music for this Exercise</a>
</center>

In Lab 1, you got some experience with Python data types (ints, bools, strings, etc...), variables in Python, and functions in Python.  The functions you wrote were pretty basic from a mathematical perspective.  For example, the function:

$$
u(t) = t^2 + 14t -6
$$

Could be implemented in Python via the following bit of code:
```
def u(t):
    return t**2 + 14*t -6
```

Now what about a situation where there are cases?  For example the function $w(t)$:
$$
s(t) = 
\begin{cases}
12 & \text{if } t>1 \\
-12 & \text{if } t \leq 1 
\end{cases}
$$

This can be implemented in Python using `if`/`else` logic. The major idea here is to analyze cases and carry out certain actions if they are/are not satisfied.  This is best shown with an example. 

Let's say we have a variable `x` that we've assigned a value to like so: `x=5`

```
if x>5:
    print 'hello'
else:
    print 'dog'
```

In basic English, the chunk of code above says: "If x is greater than 5, print 'hello', otherwise (else), print 'dog'". The above code would print the word `dog` since `x` is not greater than 5. There are several different comparison operators that you can use to construct cases in Python:

*  `==`: is equal to
* `>`: is greater than
* `>=`: is greater than or equal to
* `<`: is less than
* `<=`: is less than or equal to

The important thing to remember about these operators is that they will all analyze to a boolean (True or False).  There is no in between.  Something either is or isn't greater than something else.  

In addition in Python you also have logical operators to compare and combine comparison statements.

* `not`: is the opposite of
* `and`: Logical AND operation
* `or`: Logical OR operation

So how would we implement the function $s(t)$ above?  Like so:

```
def s(t):
    if t>1:
        return 12
    else:
        return -12
```

What if you have multiple cases?  For example what if you have:

$$
w(x) = 
\begin{cases}
12 & \text{if } x>1 \\
-12 & \text{if } 0 \leq x \leq 1 \\
2 & \text{if }  x < 0
\end{cases}
$$

In that case you can use `elif`. For example:

```
def w(x):
    if x > 1:
        return 12
    elif x >= 0 and x <= 1:
        return -12
    else: # (x <0)
        return 2
```

<python>
split_point = 0
slope_1 = cs_random.randint(1,15)

</python>

<h2>Now it is your turn...</h2>

Write a Python function to express the algebraic function $f(x)$:

$$
f(x) =
  \begin{cases}
   @{slope_1}x & \text{if }  x \leq 0 \\
   x^2       & \text{if } x > 0
  \end{cases}
$$
<question pythoncode>
csq_soln = '''def f(x):
    if x <=0:
        return %s*x
    else:
        return x**2
''' %(slope_1)

csq_initial = '''def f(x):
    pass
'''

csq_tests = [
    {'code':'ans = f(-12)'},
    {'code':'ans = f(12.344567)'},
    {'code':'ans = f(530+4)'},
    {'code':'ans = f(0.0)'},
    {'code':'ans = f(0)'},
    {'code':'ans = f(19.86)'},
    {'code':'ans = f(-19.44)'},
    ]
</question>

<python>
thresh_a = cs_random.randint(-15,-4)
thresh_b = cs_random.randint(2,15)
</python>

$$ g(x) =
  \begin{cases}
   0 & \text{if }  x < @{thresh_a} \\
   20x+100       & \text{if } @{thresh_a} \leq x \leq @{thresh_b} \\
   -10x+400 & \text{if }  x > @{thresh_b} \\
  \end{cases}
$$
<question pythoncode>
csq_soln = '''def g(x):
    if x <%s:
        return 0
    elif x >= %s and x <=%s:
        return 20*x + 100
    else:
        return -10*x+400
''' %(thresh_a, thresh_a, thresh_b)

csq_initial = '''def g(x):
    pass
'''
csq_tests = [
    {'code':'ans = g(%s)' %(thresh_a)},
    {'code':'ans = g(%s)' %(thresh_b)},
    {'code':'ans = g(530+4)'},
    {'code':'ans = g(0.0)'},
    {'code':'ans = g(0)'},
    {'code':'ans = g(19.86)'},
    {'code':'ans = g(-19.44)'},
    ]

</question>
<python>
thresh_one = cs_random.randint(-15,-4)
thresh_two = cs_random.randint(2,15)
val_1 = cs_random.randint(2,15)
val_2 = cs_random.randint(36,109)
</python>

Fantastic. Try another...

$$
 h(x) =
  \begin{cases}
   @{val_1} & \text{if }  x < @{thresh_one} \\
   @{val_2}x       & \text{if } @{thresh_one} \leq x \leq @{thresh_two} \\
   -35x & \text{if }  x > @{thresh_two} \\
  \end{cases}
$$
<question pythoncode>
csq_soln = '''def h(x):
    if x <%s:
        return %s
    elif x >= %s and x <= %s:
        return %s*x
    else:
        return -35*x
''' %(thresh_one,val_1,thresh_one,thresh_two,val_2)

csq_initial = '''def h(x):
    pass
'''
csq_tests = [
    {'code':'ans = h(%s)' %(thresh_one)},
    {'code':'ans = h(%s)' %(thresh_two)},
    {'code':'ans = h(%s)' %(val_1)},
    {'code':'ans = h(0.0)'},
    {'code':'ans = h(0)'},
    {'code':'ans = h(19.86)'},
    {'code':'ans = h(-19.44)'},
    ]
</question>


