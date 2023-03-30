
# this is a comment line, it will not be executed.

# 0110100101011010 - needs to be type
# integer
# float
# string
# boolean

# assigning data to a variable

variable1 = 110  # integer
variable2 = 110.01  # float
variable3 = "110"  # string
variable4 = True  # or False for boolean

print(variable1)
print(variable2)
print(variable3)
print(variable4)


# concatenating strings

print("This is a string"  + variable3)
print("This is a string" , variable3)

# mathematical operators

numvar1 = 12
numvar2 = 5

print(numvar1 + numvar2)  # addition
print(numvar1 - numvar2)  # subtration
print(numvar1 * numvar2)  # multiplication
print(numvar1 / numvar2)  # division
print(numvar1 ** numvar2) # to the power of

# Getting interactive data from a user

inputvar1 = input("Prompt goes in here: ") # Only return as a string data type
print(inputvar1)

help(inputvar1)

# Typecasting, changing the data type of stored data

# str()   # changes to a string
# int()   # changes to an integer
# float() # changes to a float
# bool()  # changes to a boolean
 
inputvar1asanint = int(inputvar1)
totalvar = inputvar1asanint + 1
print(totalvar)

# Computational thinking

#  Decomposition - Breaking down a problem to small parts
#  Pattern Recognition - looking for similarities, applying tools you know to them
#  Abstraction  - focussing on the relevent part of the problem 
#  Algorithms - developing a solution, using Sequencing, Selection, Iteration

# Selection

# the if statement

# if <test>:
#    code to run if the test was True

#  var1 == var2   # testing if var1 is exactly equal to / comparison
#  var1 > var2    # more than
#  var1 >= var2   # greater than or equal too
#  var1 < var
#  var1 <= var2
#  var1 != var2   # does not equal 

if inputvar1asanint == 12:
    print("12 is equal to " + inputvar1)
else:
    print(inputvar1 + " is not equal to 12")

if inputvar1asanint < 10:
    print(inputvar1 + " has one number" )
elif inputvar1asanint < 100:
    print(inputvar1 + " has two numbers" )
elif inputvar1asanint < 1000:
    print(inputvar1 + " has three numbers" )
else:
    print(inputvar1 + " has more than 3 numbers")

    # Logical Operators, and, or, not

if inputvar1asanint > 0 and inputvar1asanint < 100:
    print(inputvar1 + " has up to two charactors")

if not (inputvar1asanint > 0 and inputvar1asanint < 100):
    print(inputvar1 + "does not has up to two charactors")

