# A dictionary is a collection of key-value pairs. It's like a real-life dictionary where you have words (keys) and their definitions (values). Dictionaries are unordered, and the keys must be unique.

person = {
    "name": "Waleed",
    "age": 30,
    "city": "Dubai"
}

# You can access values in a dictionary using their corresponding keys.

print(person["name"])  # Output: Waleed

# You can add, modify, or remove key-value pairs.

person["job"] = "Software Developer"  # Adds a new key-value pair
person["age"] = 31  # Modifies the value for the key "age"
del person["city"]  # Removes the key "city"

# Dictionary Methods:
# keys(): Returns all the keys in the dictionary.
# values(): Returns all the values in the dictionary.
# items(): Returns all key-value pairs as tuples.

print(person.keys())  # Output: dict_keys(['name', 'age', 'job'])
print(person.values())  # Output: dict_values(['Waleed', 31, 'Software Developer'])



