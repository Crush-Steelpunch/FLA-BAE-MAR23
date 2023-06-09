
# Functions are great for code-re usability, thus reducing code duplication, as well as readability, even if you use a function only once, it aids in readability because you pick up what a block is doing by the function name. And because they are encapsulated it helps in testing code without effecting the rest. - Sam Dhillon

# example function 

def function_name():
    # code to run
    print("My function")

# functions can take input using variables

def grade_my_score(func_invar):
    b1 = 100
    b2 = 200
    b3 = 300
    b4 = 400
    if func_invar < b1:
        print("band b1")
    elif func_invar < b2:
        print("band b2")
    elif func_invar < b3: 
        print("band b3")
    else:
        print("band b4")

function_name()


testin = int(input("Enter a number between 0 and 500: "))

grade_my_score(testin)


# Functions can return data back to the main code

def return_my_score(func_invar):
    b1 = 100
    b2 = 200
    b3 = 300
    b4 = 400
    if func_invar < b1:
        return "band b1"
    elif func_invar < b2:
        return "band b2"
    elif func_invar < b3: 
        return "band b3"
    else:
        return "band b4"

nexttestin = int(input("Enter a number between 0 and 500: "))

resultvar  = return_my_score(nexttestin)
print(resultvar)