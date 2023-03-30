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