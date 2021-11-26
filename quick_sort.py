"""
Module containing quick sort implementations

Based on the divide and conquer approach, this sorting method is fast

Three ways of selecting the pivot and each way being either recursive or iterative

Median-of-three pivot  --->  Recursive function
Random pivot           --->  Iterative function
Pivot = array[0]       --->  Recursive function
"""
from main import menu

tests = [3, 2]

f = "first element"
m = "median of three elements"


def quicksort(numbers, first, last, pivot_selection):
    if first < last:
        if pivot_selection == "first element":
            swap(numbers, first, last)
        if pivot_selection == "median of three elements":
            swap(numbers, get_median(numbers), last)
        pivot = partition_x(numbers, first, last)
        quicksort(numbers, first, pivot - 1, pivot)
        quicksort(numbers, pivot + 1, last, pivot)
    return numbers


def partition_x(numbers, first, last):
    i = first - 1  # i indicates the index less than the pivot
    for j in range(first, last):  # assuming the pivot is the last element
        if numbers[j] <= numbers[last]:
            i += 1
            swap(numbers, i, j)
    swap(numbers, i + 1, last)
    return i + 1


def get_median(numbers):
    first = numbers[0]
    last = numbers[-1]
    mid = numbers[len(numbers) // 2]
    if mid <= first <= last: return 0
    if mid >= first >= last: return 0
    if first <= last <= mid: return -1
    if first >= last >= mid: return -1
    if first <= mid <= last: return len(numbers) // 2
    if first >= mid >= last: return len(numbers) // 2


def swap(my_list, pos1, pos2):
    p1 = my_list[pos1]
    p2 = my_list[pos2]
    my_list[pos1], my_list[pos2] = p2, p1


o = quicksort(menu(20), 0, len(menu(20)) - 1, m)
print(o)


def partition(arr, l, h):
    i = (l - 1)
    x = arr[h]

    for j in range(l, h):
        if arr[j] <= x:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return i + 1


# Function to do Quick sort
# arr[] --> Array to be sorted,
# l  --> Starting index,
# h  --> Ending index
def quickSortIterative(arr, l, h):
    # Create an auxiliary stack
    size = h - l + 1
    stack = [0] * size

    # initialize top of stack
    top = -1

    # push initial values of l and h to stack
    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h

    # Keep popping from stack while is not empty
    while top >= 0:

        # Pop h and l
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1

        # Set pivot element at its correct position in
        # sorted array
        p = partition(arr, l, h)

        # If there are elements on left side of pivot,
        # then push left side to stack
        if p - 1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1


# print(quicksort_median(menu(1000000)))


# fastest simple sorting algorithm for a large number of inputs containing duplicates
# but in terms of space complexity, creating additional arrays by the algorithm makes it less chosen than quick sort

def quicksort_median(numbers):
    if len(numbers) <= 1:
        return numbers
    smaller = []
    same = []
    larger = []
    pivot = get_median(numbers)
    for x in numbers:
        if x < pivot:
            smaller.append(x)
        if x > pivot:
            larger.append(x)
        if x == pivot:
            same.append(x)
    quicksort_median(smaller)
    quicksort_median(larger)
    numbers.clear()
    numbers += smaller
    numbers += same
    numbers += larger
    return numbers
