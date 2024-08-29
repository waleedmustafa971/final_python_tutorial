# Tuples are similar to lists but are immutable, meaning once created, you cannot modify them. Tuples are useful when you need a collection of items that should not change throughout the program.

coordinates = (10, 20)

print(coordinates[0])  # Output: 10


# Tuples are often used to store related data, such as coordinates or settings, that don't need to be modified.
# Tuples are also useful when you need to return multiple values from a function.
def get_coordinates():
    return (10, 20)
    