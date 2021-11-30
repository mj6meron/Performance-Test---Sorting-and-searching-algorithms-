"""
Module containing quick sort implementations

Based on the divide and conquer approach, this sorting method is fast

Three ways of selecting the pivot and each way being either recursive or iterative

First element pivot    --->  Recursive function
Median-of-three pivot  --->  Recursive function
Random pivot           --->  Iterative function
"""
import random
import sys

sys.setrecursionlimit(1000000)


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

        p = partition(numbers, first, last, pivot_selection)
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


def partition(numbers, first, last, pivot_selection):
    if pivot_selection == "first element":
        numbers[first], numbers[last] = numbers[last], numbers[first]
    if pivot_selection == "median of three elements":
        numbers[get_median(numbers)], numbers[last] = numbers[last], numbers[get_median(numbers)]
    if pivot_selection == "random element":
        random_pivot = random.randint(first, last)
        numbers[random_pivot], numbers[last] = numbers[last], numbers[random_pivot]
    i = (first - 1)  # index of smaller element
    pivot = numbers[last]  # pivot
    for j in range(first, last):
        if numbers[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            numbers[i], numbers[j] = numbers[j], numbers[i]
    numbers[i + 1], numbers[last] = numbers[last], numbers[i + 1]
    return i + 1


def quickSort(array, first, end, pivot_selection):
    if len(array) == 1:
        return array
    if first < end:
        pivot = partition(array, first, end, pivot_selection)

        # Separately sort elements before
        # partition and after partition
        quickSort(array, first, pivot - 1, pivot_selection)
        quickSort(array, pivot + 1, end, pivot_selection)
    return array
