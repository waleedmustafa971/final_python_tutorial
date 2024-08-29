# A set is an unordered collection of unique items. Sets are useful when you need to store non-duplicate elements and perform set operations like union, intersection, and difference.

#creating sets
numbers = {1, 2, 3, 4, 5}

# You can add or remove elements from a set.

numbers.add(6)  # Adds 6 to the set
numbers.remove(3)  # Removes 3 from the set

# Set Operations:
# Union: Combines two sets (includes all elements).
# Intersection: Returns common elements between sets.
# Difference: Returns elements that are in one set but not the other.

evens = {2, 4, 6}
odds = {1, 3, 5}

union_set = evens.union(odds)  # {1, 2, 3, 4, 5, 6}
intersection_set = evens.intersection(numbers)  # {2, 4}
difference_set = numbers.difference(evens)  # {1, 5}


