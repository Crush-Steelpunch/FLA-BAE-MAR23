
# Selection 

from base64 import b16decode


var1 = 12
var2 = 14

#if <test true or false>:
#    # this code will run if the test is true
#    print("The test resulted with true")

if var1 == var2:
    print("The test resulted with true")

# Testing Many things

var1 = 12
var2 = 14
var3 = 8
var4 = 27
var5 = 3081

if var1 > var2:
    print("The test resulted with true")
else:    
    print("The test resulted with false")
    
if var1 > var3:
    print("The test resulted with true")
else:    
    print("The test resulted with false")

if var1 > var4:
    print("The test resulted with true")
else:    
    print("The test resulted with false")
if var1 > var5:
    print("The test resulted with true")
else:    
    print("The test resulted with false")

# using elif

    
var1 = 30
var2 = 14
var3 = 8
var4 = 27
var5 = 3081


if var1 > var2:
    print("var 1 is not the smallest")
elif var1 > var3:
    print("var 1 is not the smallest")
elif var1 > var4:
    print("var 1 is not the smallest")
elif var1 > var5:
    print("var 1 is not the smallest")
else:
    print("var 1 is the smallest")

# Alternative elif

b1 = 100
b2 = 200
b3 = 300
b4 = 400

testin = int(input("Enter a number between 0 and 500: "))

if testin < b1:
    print("band b1")
elif testin < b3:
    print("band b3")
elif testin < b2: # sequence means this test will never be run
    print("band b2")
else:
    print("band b4")


# better test sequence

if testin < b1:
    print("band b1")
elif testin < b2:
    print("band b2")
elif testin < b3: 
    print("band b3")
else:
    print("band b4")


# alternative test sequence using logical operators


if testin < b1:
    print("band b1")
elif testin < b3 and testin > b2:
    print("band b3")
elif testin < b2: 
    print("band b2")
else:
    print("band b4")


# logical operators

# and, or, not

if not testin == 150:
    print("testin is not equal to 150")