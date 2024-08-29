# Attributes: Variables that hold data specific to an object. They are defined inside the __init__ method (the constructor) and accessed using self.
# Methods: Functions that define the behaviors of an object. They operate on the object's attributes.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start_engine(self):
        print(f"The {self.brand} {self.model}'s engine is starting!")

my_car = Car("Toyota", "Corolla")
my_car.start_engine()  # Output: The Toyota Corolla's engine is starting!
