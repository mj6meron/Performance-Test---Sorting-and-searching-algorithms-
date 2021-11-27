from main import menu
from merge_sort import merge_sort

n = [2, 3, 4, 10, 40, 45, 89, 75, 10, 2, 3, 54, 65, 85, 47, 52, 14]


def binary_search(arr, low, high, x):
    # Check base case -> if list is not empty while on recursion
    if high >= low:
        mid = (high + low) // 2
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        # Else the element can only be present in right sub array
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        # Element is not present in the array
        return -1


def search(arr, x):
    return binary_search(arr, arr[0], len(arr) - 1, x)

