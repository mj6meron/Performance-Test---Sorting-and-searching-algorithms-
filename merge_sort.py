"""
Module containing merge sort implementation

Tail Recursive function

Merge sort uses the divide and conquer technique
So the fist step is to use recursion to divide the list into individual elements
Then as the recursion tends to reverse then we start merging and sorting
"""

from main import menu


def merge_sort(numbers_list):
    if len(numbers_list) <= 1:
        return numbers_list
    middle_index = len(numbers_list) // 2
    left_list = merge_sort(numbers_list[:middle_index])
    right_list = merge_sort(numbers_list[middle_index:])
    """ Where the magic happens - merging back and sorting"""
    sorted_numbers = []
    left_index = 0
    right_index = 0
    while left_index < len(left_list) and right_index < len(right_list):
        if left_list[left_index] < right_list[right_index]:
            sorted_numbers.append(left_list[left_index])
            left_index += 1
        else:
            sorted_numbers.append(right_list[right_index])
            right_index += 1
    sorted_numbers += left_list[left_index:]
    sorted_numbers += right_list[right_index:]
    return sorted_numbers
