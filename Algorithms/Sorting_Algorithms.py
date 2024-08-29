# 1-Bubble Sort:
# A simple comparison-based algorithm.
# Repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.
# Time Complexity: O(n^2)

# 2- Insertion Sort:
# Builds the final sorted array one item at a time.
# Good for small datasets.
# Time Complexity: O(n^2)

# 3- Merge Sort:
# A divide-and-conquer algorithm.
# Divides the array into halves, recursively sorts them, and then merges them back.
# Time Complexity: O(n log n)

# 4- Quick Sort:

# Also a divide-and-conquer algorithm.
# Picks a pivot element and partitions the array into two halves such that elements less than the pivot are on one side, and elements greater than the pivot are on the other.
# Time Complexity: O(n log n) on average

####################

# Let's implement one of these sorting algorithms, Bubble Sort, in Python:

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Track whether a swap was made in this iteration
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no swap was made, the array is already sorted
        if not swapped:
            break
    return arr

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
print("Sorted array:", sorted_arr)
