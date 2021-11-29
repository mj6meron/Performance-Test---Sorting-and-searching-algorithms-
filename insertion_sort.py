"""
Module containing insertionSort implementation

Interactive function

pseudo code :
    for elements in the number_list
        store current element
        get previousIndex
        while previousIndex >= 0 and currentElement < previousElement
            over wright previousElement into current index
            decrement previous index ( technically do the insertion)
        Over wright previousElement with the currentValue we stored

"""

# from main import menu as menu


def insertion_sort(number_list):
    for x in range(len(number_list)):
        current = number_list[x]
        previousIndex = x - 1
        while previousIndex >= 0 and current < number_list[previousIndex]:
            number_list[previousIndex + 1] = number_list[previousIndex]
            previousIndex -= 1
        number_list[previousIndex + 1] = current
    return number_list

