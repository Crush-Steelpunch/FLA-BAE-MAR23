# Iteration

# while statement

# while <test>:
#     codetorun()

# You must change the var being tested inside the loop

testvar1 = 15
while testvar1 != 10:
    print(str(testvar1) + " is not equal to 10" )
    testvar1 = int(input("Guess what number you should type"))

# while True:
#    print("Infinate Looooooop!")

# incrementing a varable

while testvar1 != 40:
    print(str(testvar1) + " is not equal to 40" )
    testvar1 = testvar1 + 1   # Or testvar1 += 1





# Breaking Loops

while testvar1 != 10:
    print(str(testvar1) + " is not equal to 10" )
    testvar1 = int(input("Guess what number you should type"))
    if testvar1 == 13:
        print("Lucky 13!")
        break

# too poor to finish a guessing game
countvar = 0
while testvar1 != 10:
    print(str(testvar1) + " is not equal to 10" )
    countvar = countvar + 1
    testvar1 = int(input("Guess what number you should type"))
    if countvar == 13:
        print("Lucky 13! You had too many guesses!")
        break


print("end program")


# range function

# range(start)

#  Return an object that produces a sequence of integers from start (inclusive)
#|  to stop (exclusive) by step.

# range(5)       0,1,2,3,4
# range(5,10)    5,6,7,8,9
# range(0,10,2)  0,2,4,6,8

# for loop

# for variable in sequence:
#     code()

for var  in range(5):
    print("This line")
 

for loopvar1 in range(10):
    print("This is line " + str(loopvar1))


for loopvar1 in range(0,20,2):
    print("This is line " + str(loopvar1))
    if loopvar1 == 12:
        break 

# nested loop

for outervar in range(10):
    print("This is section " + str(outervar))
    for innervar in range(3):
        print("+--- This is subsection " + str(innervar) + " of " + str(outervar) )

