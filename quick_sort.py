"""
Module containing quick sort implementations

Based on the divide and conquer approach, this sorting method is fast

Three ways of selecting the pivot and each way being either recursive or iterative

Median-of-three pivot  --->  Recursive function
Random pivot           --->  Iterative function
Pivot = array[0]       --->  Recursive function
"""
from main import menu

tests = [4, 5, 8, 2, 3, 1]


def quicksort(numbers, first, last):
    if first >= last:
        return numbers
    pivot = partition_x(numbers, first, last)
    print('hi')
    print(quicksort(numbers, first, pivot - 1))

    print('hello')
    quicksort(numbers, pivot + 1, last)
    return numbers



def partition_x(numbers, first, last):
    pivot = numbers[0]
    swap(numbers, 0, last)
    i = first - 1  # i indicates the index less than the pivot
    for j in range(0, last - 1):
        if numbers[j] <= pivot:
            i += 1
            swap(numbers, i, j)
    swap(numbers, i + 1, last)
    return i + 1


def swap(my_list, pos1, pos2):
    p1 = my_list[pos1]
    p2 = my_list[pos2]
    my_list[pos1], my_list[pos2] = p2, p1


x = quicksort(tests, 0, len(tests) - 1)
print(x)


def quicksort_median(numbers):
    pass


def get_median(numbers):
    first = numbers[0]
    last = numbers[-1]
    mid = numbers[len(numbers) // 2]
    if mid <= first <= last: return first
    if mid >= first >= last: return first
    if first <= last <= mid: return last
    if first >= last >= mid: return last
    if first <= mid <= last: return mid
    if first >= mid >= last: return mid


def quicksort_randomile(numbers):
    pass


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
