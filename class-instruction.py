
from tkinter import W


class Nummaths:

    mathvar = 5

    def addnum(self, invar):
        return invar + self.mathvar

    def subnum(self, invar):
        return invar - self.mathvar

mathvar = Nummaths()
anothervar = Nummaths()
anothervar.mathvar = 10
thisisanobject = Nummaths()
thisisanobject.mathvar = 30

print(mathvar.addnum(7))
print(mathvar.subnum(7))
print(anothervar.addnum(7))
print(anothervar.subnum(7))
print(thisisanobject.addnum(7))
print(thisisanobject.subnum(7))

# using an init function to make things set up correctly


class Nummaths2:

    def __init__(self,setnum):
        self.mathvar = setnum        

    def addnum(self, invar):
        return invar + self.mathvar

    def subnum(self, invar):
        return invar - self.mathvar

    
mathvar = Nummaths2()
anothervar = Nummaths2(10)
thisisanobject = Nummaths2(30)


print(mathvar.addnum(7))
print(mathvar.subnum(7))
print(anothervar.addnum(7))
print(anothervar.subnum(7))
print(thisisanobject.addnum(7))
print(thisisanobject.subnum(7))

# Passing data between instances of objects

class Vis:
        
        def __init__(self, invar,mydata):
                    self.invar = invar
                    self.mydata = mydata
                                
        def showme(self):
            print(self)

        def copytome(self,objectin):
            print(objectin)
            self.mydata = objectin.invar
                                                                            

object1 = Vis("this","")
print(object1)
object1.showme()
object2 = Vis("that","")
print(object2)
object2.showme()

object2.copytome(object1)
print(object2.mydata

