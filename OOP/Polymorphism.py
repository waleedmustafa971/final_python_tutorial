# Polymorphism allows methods in different classes to have the same name but behave differently based on the object that calls them.

# Inheritance allows you to create a new class based on an existing class. The new class (child) inherits attributes and methods from the existing class (parent), and you can add or override them as needed.

class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print(f"{self.name} is making a sound!")

class Dog(Animal):  # Dog inherits from Animal
    def make_sound(self):
        print(f"{self.name} is barking!")



# Here, Dog inherits the name attribute and the make_sound() method from the Animal class but overrides the make_sound() method to provide a specific implementation.



class Cat(Animal):
    def make_sound(self):
        print(f"{self.name} is meowing!")

animals = [Dog("Buddy"), Cat("Whiskers")]

for animal in animals:
    animal.make_sound()

# In this example, both Dog and Cat have a make_sound() method, but they behave differently when called on their respective objects.