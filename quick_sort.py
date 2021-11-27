"""
Module containing quick sort implementations

Based on the divide and conquer approach, this sorting method is fast

Three ways of selecting the pivot and each way being either recursive or iterative

First element pivot    --->  Recursive function
Median-of-three pivot  --->  Recursive function
Random pivot           --->  Iterative function
"""
import random
from main import menu
import sys

sys.setrecursionlimit(2000000)
"""pivot selection menu"""
f = "first element"
m = "median of three elements"
r = "random element"


def quicksort_recursive(numbers, first, last, pivot_selection):
    if first < last:
        pivot = partition_x(numbers, first, last, pivot_selection)
        quicksort_recursive(numbers, first, pivot - 1, pivot)
        quicksort_recursive(numbers, pivot + 1, last, pivot)
    return numbers


def quicksort_iterative(numbers, first, last, pivot_selection):
    size = last - first + 1
    stack = [0] * size
    top = -1
    top = top + 1
    stack[top] = first
    top = top + 1
    stack[top] = last
    while top >= 0:
        last = stack[top]
        top = top - 1
        first = stack[top]
        top = top - 1

        p = partition_x(numbers, first, last, pivot_selection)
        if p - 1 > first:
            top = top + 1
            stack[top] = first
            top = top + 1
            stack[top] = p - 1
        if p + 1 < last:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = last
    return numbers


def partition_x(numbers, first, last, pivot_selection):
    if pivot_selection == "first element":
        numbers[first], numbers[last] = numbers[last], numbers[first]
    if pivot_selection == "median of three elements":
        numbers[get_median(numbers)], numbers[last] = numbers[last], numbers[get_median(numbers)]
    if pivot_selection == "random element":
        random_pivot = random.randint(first, last)
        numbers[random_pivot], numbers[last] = numbers[last], numbers[random_pivot]
    i = first - 1  # i indicates the index less than the pivot
    for j in range(first, last):  # assuming the pivot is the last element + last not included
        if numbers[j] <= numbers[last]:
            i += 1
            numbers[j], numbers[i] = numbers[i], numbers[j]
    numbers[i + 1], numbers[last] = numbers[last], numbers[i + 1]
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


o = menu(100000)
quicksort_recursive(o, 0, len(o) - 1, f)
print("firstPivot recursive")
# quicksort_recursive(o, 0, len(o) - 1, m)
print("median recursive")
randomPivot = quicksort_iterative(o, 0, len(o) - 1, r)
print("random iterative")
# print(randomPivot)

"""
Fast simple sorting algorithm
For a large number of inputs containing duplicates
----  space complexity  ------ 
Creating additional arrays by the algorithm makes it less chosen than quick sort
"""


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
