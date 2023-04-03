from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def eat(self):
        pass


class Bird(Animal):

    def tweet(self):
        return "peet peet peet"

    def eat(self,worms):
        return birdpoo

pipistrol = Bird()

print(pipistrol.tweet())


