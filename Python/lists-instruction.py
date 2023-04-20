
# lists

       # index    0       1        2
coloursvar1 = [ "red", "blue", "yellow" ]

numbersvar1 = [ 5 , 47 , 209 ]

boolsvar1 = [ True, False, True, True ] 

print(coloursvar1)
print(numbersvar1)
print(boolsvar1)


# iterating on a list

for item in coloursvar1:
    print("list colour: " + item)

# addressing a list by using an index

print(coloursvar1[0])
print(coloursvar1[2])
print(coloursvar1[1])

print(numbersvar1[2])

# discovering list lenght with len()

print(len(coloursvar1))

# iterating lists with a while loop

listlen = len(numbersvar1)
counter = 0
while counter < listlen : 
    print(numbersvar1[counter])
    counter += 1


# Another type of list. Strings are a type of list


wordvar = "spleleodot"
for letter in wordvar:
    print(letter)

print(wordvar[0])
print(wordvar[5])

print(len(wordvar))

# list methods


coloursvar1 = [ "red", "blue", "yellow" ]

coloursvar1.append("brown")
print(coloursvar1)
coloursvar1.append("blue")
print(coloursvar1)
coloursvar1.append("pink")
print(coloursvar1)
coloursvar1.reverse()
print(coloursvar1)
coloursvar1.remove("red")
print(coloursvar1)
coloursvar1.sort()
print(coloursvar1)

# testing things in lists using 'in'

if "pink" in coloursvar1:
    print("pink is in the list")

if "burgundy" in coloursvar1:
    print("burgundy is in the list")
else:
    print("burgundy is not in the list")

    # Converting things to lists.

shoppinglist = input("Type in your shoppinglist on one line: ")
print(shoppinglist)

  #|  split(self, /, sep=None, maxsplit=-1)
  #    Return a list of the substrings in the string, using sep as the separator string.

shoppingitemslist = shoppinglist.split(",")

print(shoppingitemslist)
print(len(shoppingitemslist))