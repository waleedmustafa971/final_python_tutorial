# You can also implement binary search using recursion:

def recursive_binary_search(arr, low, high, target):
    if high >= low:
        mid = (low + high) // 2

        # If the element is present at the middle
        if arr[mid] == target:
            return mid
        # If the element is smaller than mid, search the left half
        elif arr[mid] > target:
            return recursive_binary_search(arr, low, mid - 1, target)
        # Else search the right half
        else:
            return recursive_binary_search(arr, mid + 1, high, target)
    else:
        # Element is not present in the array
        return -1

    # Example usage
    arr = [2, 3, 4, 10, 40]
    target = 10
    result = recursive_binary_search(arr, 0, len(arr) - 1, target)

    if result != -1:
        print("Element is present at index", result)
    else:
        print("Element is not present in array")



# This is a more elegant approach but might not be as memory-efficient as the iterative version due to the overhead of recursive calls.
