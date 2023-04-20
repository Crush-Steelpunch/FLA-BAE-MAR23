# This line starts with a # which means it is a comment line
# not going to be run as code

print("Hello World")


# Data Types

# what is it? 0101101011011

# Binary?
# Integer?
# Float? 
# phone number
# list of boolean

var1 = 101101011011 # this is an int
var2 = "0101101011011" # this is a string
var3 = 101101011011.0  # this is a float
var4 = True # this is a boolean

# Interactive putting data in a variable

var5 = input("example prompt text: ")


# Mini program with input
firstname = input("Type your name: ")
print("Hello " + firstname )


#coolnessrating = input("Type your coolnessrating: ")
coolnessrating = "85"  # cannot concatenate differetn types
print("You are " + coolnessrating + "% cool")


# Chaning gariable type

# str(), int(), float() to change a var type

yourage = input("Type in your age: ")
nextyearage = int(yourage) + 1
print("Next year you will be " + str(nextyearage))

