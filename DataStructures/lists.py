# A list is an ordered collection of items that can be of any data type (integers, strings, etc.). Lists are mutable, meaning you can modify them after creation.

fruits = ["apple", "banana", "cherry"]

# You can access list elements using their index, starting from 0.

print(fruits[0])  # Output: apple

# You can add, remove, or modify elements in a list.

# Append: Adds an element to the end of the list.
# Insert: Adds an element at a specific position.
# Remove: Removes the first occurrence of a specific element.
# Pop: Removes an element at a specific index (or the last element if no index is provided).

fruits.append("orange")  # Adds orange to the end of the list
fruits.insert(1, "kiwi")  # Inserts kiwi at index 1
fruits.remove("banana")  # Removes banana from the list
last_fruit = fruits.pop()  # Removes and returns the last item (orange)

# You can retrieve a portion of the list using slicing:

subset = fruits[1:3]  # Retrieves elements from index 1 to 2

# len(): Returns the number of items in the list.
# sort(): Sorts the list in place.
# reverse(): Reverses the order of the list in place.





