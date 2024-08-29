# What is Divide and Conquer?
# Divide and Conquer is a strategy that breaks a problem down into smaller subproblems, solves them independently, and then combines the solutions to solve the original problem. This approach is particularly useful for recursive algorithms.

# Key steps:

# Divide: Break the problem into smaller subproblems.
# Conquer: Solve the subproblems recursively.
# Combine: Combine the solutions of the subproblems to form the solution of the original problem.

# Classic Examples:
# Merge Sort: This is a classic example of the divide and conquer strategy. We have already discussed this earlier.
# Quick Sort: Another divide and conquer sorting algorithm that we introduced before.
# Binary Search: Although a searching algorithm, binary search also uses divide and conquer by halving the search space at each step.

    # Here's how you can implement Binary Search in Python:

    # Binary search is an efficient algorithm for finding an item from a sorted list of items. It repeatedly divides the search space in half until the item is found or the search space is exhausted.

    # Time Complexity: O(log n)

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  # Element found
        elif arr[mid] < target:
            low = mid + 1  # Search in the right half
        else:
            high = mid - 1  # Search in the left half

    return -1  # Element not found

# Example usage
arr = [2, 3, 4, 10, 40]
target = 10
result = binary_search(arr, target)

if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")


# In this implementation:

# We divide the array in half.
# Depending on whether the target value is greater or smaller than the middle value, we narrow our search to one of the halves.
# We continue this process until we find the target or exhaust the search space.
