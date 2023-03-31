# Python Functions

# built in functions https://docs.python.org/3.10/library/functions.html

#len()
#str()
#int()
#float()
#bool()

# Pass literals, variables, expressions to functions

print(1+1)
cheese = "brie"
print(cheese)

# Objects (e.g. variables) can have method functions

list1 = ["meat", "vegetables","cake"]
list1.sort()
print(list1)
print(list1.count("cake"))
list1.append("party rings")
print(list1)

age = input("Type age: ")
if age.isnumeric():
    print("Number")
else:
    print("Not a num, numbskull")


    # Importing modules for added functionallity

import math

numvar1 = int(input("Type a number"))
sqrtvar1 = math.sqrt(numvar1)
print(round(sqrtvar1,2))

# print(sqrt(5)) cant just use the function without referencing the module


# import using from so you don't have to reference 
# the module name each time

from math import sqrt

print(sqrt(5))

