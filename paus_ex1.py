"""
This is a multiline string
It is used by docstring
We will cover it later in depth
"""

print("Hello world!")
print()
print("Hello world for the second time")
print()
print("Hello", "world!!!")
print()
print("Hello", 'world', "!!!")
print("One of my favourite books is 'Python for programmers'")
print()
print('Actually, there are more books, including "Python for programmers by Deitel" ')
print()
print("Actually, there are more books, including 'Python for programmers by Deitel' ")
print("Hello", "world", "for", "the", "time", "being", sep="\n")

# This is my first comment
# It is a variable that is being used by the print statement

x = "This is my first variable using a simple print()."
print(x)
print(x)
print(x)

y = 53
print(type(y))
print("Y value is equeal to " + str(y))
print(type(y))

print("Let's try to convert in the opposite direction: string to a number")
z = "123"
z = int(z)
print(type(z))

f = 123.932342342
print(f)
print(type(f))
print(int(f))
print(float(y))

#Introduction of isinstance function
print("Intro to isinstance function")
print(type(f))
print(isinstance(f, float))

#Boolean data type
b = False
print(type(b))

#imaginary numbers
i = 5 + 5j
print(i)
print(type(i))

#swapping values in python
x = 10
y = 20
x, y = y, x
print(x, y, sep=" ")

#crazy number
x = 444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444445555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555566666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666677777777777777777777777777777777777777777777777777777777777777777777777777777777
print(x)

#scientific notation
y = 9e15
print(type(y))

#using bool() casting on various data types
print(bool(0))
print(bool(" "))

#None data type
example = None
print(example)
print(type(example))

#math operations
print(234//11)
#modulus operator produces reminder
print(11%10)
#power operand
print(2**64)

#math functions
result = max(12, 333, 445, 2, 44)
print(result)
print(min(2, 33, 55, 1, 6666, result))
negative_day = -3455
print(abs(negative_day))
print(pow(2,10))
print(round(0.257, 2))

# using math module
import math
print(math.sqrt(81))
print(math.e)
print(math.pi)
print(math.ceil(3.1))
print(round(3.1))
print(math.floor(3.9))
print(round(math.pi, 2))

#assignment operators
c = 10
#c = c + 11
c += 11
print(c)



