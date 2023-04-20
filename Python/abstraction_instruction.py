""" import ABC and abstract method from class abc """

from abc import ABC, abstractmethod

class Animal(ABC):
    """
    
    This class is to define an animal

    """
    @abstractmethod
    def eat(self,food):
        """
        This function is the eat method

        Parameter: food (str)
        """
    def flap(self):
        """
        This function is the flap method

        """
        return "Aaaand, FLAP!"

class Bird(Animal):
    """
    
    This class is to define an Bird, inherits from Animal

    """
    def tweet(self):
        """
        This function is the tweet method
        """
        return "peet peet peet"

    def eat(self,food):
        birdpoo = food
        return birdpoo

pipistrol = Bird()

print(pipistrol.tweet())

help(pipistrol)
