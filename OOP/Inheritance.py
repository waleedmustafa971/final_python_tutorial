# Inheritance allows you to create a new class based on an existing class. The new class (child) inherits attributes and methods from the existing class (parent), and you can add or override them as needed.

class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print(f"{self.name} is making a sound!")

class Dog(Animal):  # Dog inherits from Animal
    def make_sound(self):
        print(f"{self.name} is barking!")

my_dog = Dog("Buddy")
my_dog.make_sound()  # Output: Buddy is barking!

# Here, Dog inherits the name attribute and the make_sound() method from the Animal class but overrides the make_sound() method to provide a specific implementation.

