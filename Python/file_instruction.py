# open with read
textvar = open('text-file.txt')

print(textvar)

textstream = textvar.read()
textvar.close()

print(textstream)

textstream = "\n\nThis is a new line of text\nAdded to the start .\n\n" + textstream 

print(textstream)

writetextvar = open('text-file.txt',mode='w')

writetextvar.write(textstream)
writetextvar.close()

#openwith readlines
textvar = open('text-file.txt')

print(textvar)

textlines = textvar.readlines()
textvar.close()

textlines.append("\n")
textlines.append("This line was appended")
print(textlines)

print(textlines)

writetextlines = open('text-file.txt',mode='w')
writetextlines.writelines(textlines)
writetextlines.close()



#help(textvar)