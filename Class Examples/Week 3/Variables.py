"""
Let's revisit variables. Recall that in the last module we used them to change the
value of degrees between drawing the sun rays. This allowed us to re-use the
exact same code rather than tweaking each line. This is a time-consuming and
error-prone process. There are a number of ways to avoid repeating code but we're
talking about variables!
"""

x = 5
interest = 0.5
name = "John Doe"
answer = True
question = None

"""
All of the statements above declare and initialize variables. Each of the variables is a different
type. The first is an integer (whole number, negative or positive), the second is a floating point
variable. The third is a string which is a sequence of characters. The fourth is boolean, it can
be true or false. The last is a bit of a trick, it isn't a type but the way that Python assigns
a "non-value" to a variable. Occasionally, you will need to declare a value but are not ready to
give it a value. This is how you do it. If this doesn't make sense, hang in there, it will. 
"""
print(x) # this will print 5 because that is its value.
x = 9
print(x) # now this will print 9. Yep, variables can vary and you can change the value as needed.
x = "I'm a string now!"

""" 
now x is a string and that is what will print out. Being dynamically typed you can change the type
as well as the value. The following will print out "I'm a string now!" 
"""
print(x)

""" 
Variables can be named almost anything ... almost. You can't start a variable name with a number
and using Python keywords (i.e. print, for, each, etc.,) won't work either. Also, you can't have
spaces in variable names so a variable name "big number" won't fly. 

Beyond what you can't do, there are other things you really should and shouldn't do. In general,
variables should be descriptive. I.e a good coding practice is self-documenting code. One should
be able to look at the code, not the comments and get a good sense for what it is doing. Variable
names are a key to accomplishing this. So, yes the x I used earlier, other than for very simple 
tasks, is not recommended!

Sometimes constants make formulas confusing and it often helps to use variables in the formulas
to make them more readable. For example:

total_cost = net_cost * (1 + .06) 

is not as readable as:

total_cost = net_cost * (1 + SALES_TAX)

Here, one can read the formula and have a better understanding. Note that the all caps names are 
recommended for constants or variables that are not designed to change once defined. Again, this
is not a Python required syntax but just a good coding practice.

Python coding standards rely on underscores in variables like total_cost or net_price. The 
Python interpreter doesn't care but this is generally considered good practice in Python circles.

One last thing, variables are case sensitive. So Consumer_cost is a completely different variable
from consumer_cost. 

"""


""" Variables can be used to do calculations, suppose that: """
celsius = 0

# if we want to convert this to fahrenheit we can use a simple formula.
fahrenheit = celsius * 9.0 / 5 + 32

# This allows us to convert any value of celsius to its equivalent in fahrenheit. So let's look
# a little closer at the formula. The 9.0 / 5 is simply dividing 9.0 by 5. The + 32 is what
# one would assume, just adds 32. Python uses the same mathematical precedence rules or
# order of operations as algebra. Consequently, the 9.0 divided by 5 happens before adding 32.
# Before we leave this formula, one more thing. The 9.0 instead of 9 is on purpose. You see,
# in Python 9 / 5 is 1. If integers (whole numbers) are divided, the result is a whole number.
# The end result is that the fractions are lost. In order to keep the fractional part of the
# result, one of the values needs to be floating point or fractional. The .0 added to the 9
# will make Python treat the expression as floating point.




