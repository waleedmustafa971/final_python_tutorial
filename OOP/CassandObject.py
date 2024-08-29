# Class: A blueprint for creating objects. It defines a set of attributes and methods that the objects created from the class will have.
# Object: An instance of a class. It represents the actual entity that is created based on the class blueprint.

class Dog:
    def __init__(self, name, breed):  # Constructor method
        self.name = name              # Attribute
        self.breed = breed            # Attribute

    def bark(self):                   # Method
        print(f"{self.name} is barking!")

# Creating objects (instances of the class)
my_dog = Dog("Buddy", "Golden Retriever")
print(my_dog.name)  # Output: Buddy
my_dog.bark()       # Output: Buddy is barking!

# In this example:

# Dog is a class.
# my_dog is an object (instance) of the Dog class.
# __init__ is the constructor method that initializes the object's attributes (name and breed).
# bark() is a method that defines a behavior for the object.