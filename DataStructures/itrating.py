# You can use loops to iterate through any of these data structures:

# LISTS:

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

#Tuple:

coordinates = (10, 20)


for coordinate in coordinates:
    print(coordinate)

#Dictionary:
person = {
    "name": "Waleed",
    "age": 30,
    "city": "Dubai"
}

for key, value in person.items():
    print(key, ":", value)

#Set:

numbers = {1, 2, 3, 4, 5}


for number in numbers:
    print(number)


##################
# Summary:

# Lists: Ordered and mutable collections.
# Tuples: Ordered but immutable collections.
# Dictionaries: Unordered collections of key-value pairs.
# Sets: Unordered collections of unique items.

