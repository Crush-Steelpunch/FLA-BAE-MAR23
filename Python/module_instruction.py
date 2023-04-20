
# Functions are great for code-re usability, thus reducing code duplication, as well as readability, even if you use a function only once, it aids in readability because you pick up what a block is doing by the function name. And because they are encapsulated it helps in testing code without effecting the rest. - Sam Dhillon

# example function 

def function_name():
    # code to run
    return "My function"

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


    # polymo class
class polymo:

    def trim(self, input):
        
        # code that removes the last lettter of string
        strlen = len(input)
        newstr = input[0:strlen-1]
        return newstr


def palindrom_function(instr):
    strlenthg = len(instr)
    outstr = ''
    for letter in range(strlenthg-1,-1,-1):
        outstr = outstr + instr[letter]
    if outstr == instr:
        return True
    else:
        return False
    