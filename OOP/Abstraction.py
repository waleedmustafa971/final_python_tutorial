# Abstraction is the concept of hiding the complex implementation details and showing only the essential features of an object. This is often achieved using abstract classes in Python.

# Python provides the abc module to define abstract classes, where one or more methods are abstract and must be implemented by any subclass.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rect = Rectangle(10, 20)
print(rect.area())  # Output: 200


# In this example, Shape is an abstract class, and area() is an abstract method that must be implemented by any class that inherits from Shape.

#####################
# Summary of Key Concepts

# Class and Object: Classes are blueprints for objects.
# Attributes and Methods: Attributes hold data; methods define behaviors.
# Encapsulation: Bundling data and methods into a single unit, with control over access.
# Inheritance: Reusing code by creating new classes based on existing ones.
# Polymorphism: Defining methods that can behave differently in different classes.
# Abstraction: Hiding complexity by showing only the necessary details through abstract classes.
