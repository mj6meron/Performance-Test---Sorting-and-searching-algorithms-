""" This test file does all the performance testing"""

import timeit
import binarysearch as b
import insertion_sort as i
import merge_sort as m
import quick_sort as q
from main import menu

n_ten = menu(10)
n_hundred = menu(100)
n_oneThousand = menu(1000)
n_tenThousand = menu(10000)
n_hundredThousand = menu(100000)
n_oneMillion = menu(1000000)
inputs = [len(n_ten), len(n_hundred), len(n_oneThousand), len(n_tenThousand), len(n_hundredThousand),
          len(n_oneMillion)]
cycles = 3  # implies the cycles of test of each input
inputsN = 6  # implies the number of inputs eg,(1 says n = 10), (2 says n=10, n = 100) ... etc
sortingSetup = '''
import insertion_sort as i
from main import menu
import merge_sort as m
import quick_sort as q

n_ten = menu(10)
n_hundred = menu(100)
n_oneThousand = menu(1000)
n_tenThousand = menu(10000)
n_hundredThousand = menu(100000)
n_oneMillion = menu(1000000)

fp = "first element"
mp = "median of three elements"
rp = "random element"
        '''

binarySetup = '''
from main import menu
import merge_sort as m
import binarysearch as b

n_ten = menu(10)
n_hundred = menu(100)
n_oneThousand = menu(1000)
n_tenThousand = menu(10000)
n_hundredThousand = menu(100000)
n_oneMillion = menu(1000000)

numbers = [n_ten, n_hundred, n_oneThousand, n_tenThousand, n_hundredThousand, n_oneMillion]
sorted_numbers = []
for e in numbers: sorted_numbers.append(m.mergeSort(e))
        '''


def insertionSortTest():
    insertionInputs = ['i.insertion_sort(n_ten)', 'i.insertion_sort(n_hundred)', 'i.insertion_sort(n_oneThousand)',
                       'i.insertion_sort(n_tenThousand)', 'i.insertion_sort(n_hundredThousand)',
                       'i.insertion_sort(n_oneMillion)']
    print()
    print(
        '************************************  Insertion Sort - Iterative ********************************************')
    # pass the number of inputs by tweaking this len(insertionInputs)
    for x in range(0, inputsN):
        insertionSortRunningTime = timeit.repeat(stmt=insertionInputs[x], repeat=cycles, setup=sortingSetup, number=1)
        average = '{:.10f}'.format(sum(insertionSortRunningTime) / len(insertionSortRunningTime))
        print('Insertion sort for n = ' + str(inputs[x]))
        print('Average time: %s ' % average)
        print('------------------------------------------------------------')


def mergeSortTest():
    mergeInputs = ['m.mergeSort(n_ten)', 'm.mergeSort(n_hundred)', 'm.mergeSort(n_oneThousand)',
                   'm.mergeSort(n_tenThousand)', 'm.mergeSort(n_hundredThousand)',
                   'm.mergeSort(n_oneMillion)']
    print()
    print(
        '************************************  Merge Sort - Recursive ********************************************')
    # pass the number of inputs by tweaking this len(mergeInputs)
    for x in range(0, inputsN):
        mergeSortRunningTime = timeit.repeat(stmt=mergeInputs[x], repeat=cycles, setup=sortingSetup, number=1)
        average = '{:.10f}'.format(sum(mergeSortRunningTime) / len(mergeSortRunningTime))
        print('Merge sort for n = ' + str(inputs[x]))
        print('Average time: %s ' % average)
        print('------------------------------------------------------------')


def quickSortTest_firstPivot():
    quickSort_firstPivotInputs = ['q.quickSort(n_ten, 0, len(n_ten) - 1, fp)',
                                  'q.quickSort(n_hundred, 0, len(n_hundred) - 1, fp)',
                                  'q.quickSort(n_oneThousand, 0, len(n_oneThousand) - 1, fp)',
                                  'q.quickSort(n_tenThousand, 0, len(n_tenThousand) - 1, fp)',
                                  'q.quickSort(n_hundredThousand, 0, len(n_hundredThousand) - 1, fp)',
                                  'q.quickSort(n_oneMillion, 0, len(n_oneMillion) - 1, fp)']
    print()

    print(
        '************************************  Quick-Sort - firstPivot  ********************************************')
    # pass the number of inputs by tweaking this len(mergeInputs)
    for x in range(0, inputsN - 1):
        quicksort_firstPivot = timeit.repeat(stmt=quickSort_firstPivotInputs[x], repeat=cycles,
                                             setup=sortingSetup,
                                             number=1)
        average = '{:.10f}'.format(sum(quicksort_firstPivot) / len(quicksort_firstPivot))
        print('Quick sort for n = ' + str(inputs[x]))
        print('Average time: %s ' % average)
        print('------------------------------------------------------------')


def quickSortTest_middlePivot():
    quickSort_middlePivotInputs = ['q.quickSort(n_ten, 0, len(n_ten) - 1, mp)',
                                   'q.quickSort(n_hundred, 0, len(n_hundred) - 1, mp)',
                                   'q.quickSort(n_oneThousand, 0, len(n_oneThousand) - 1, mp)',
                                   'q.quickSort(n_tenThousand, 0, len(n_tenThousand) - 1, mp)',
                                   'q.quickSort(n_hundredThousand, 0, len(n_hundredThousand) - 1, mp)',
                                   'q.quickSort(n_oneMillion, 0, len(n_oneMillion) - 1, mp)']
    print()

    print(
        '************************************  Quick-Sort - middlePivot  ********************************************')
    # pass the number of inputs by tweaking this len(mergeInputs)
    for x in range(0, inputsN - 1):
        quicksort_middlePivot = timeit.repeat(stmt=quickSort_middlePivotInputs[x], repeat=cycles,
                                              setup=sortingSetup,
                                              number=1)
        average = '{:.10f}'.format(sum(quicksort_middlePivot) / len(quicksort_middlePivot))
        print('Quick sort for n = ' + str(inputs[x]))
        print('Average time: %s ' % average)
        print('------------------------------------------------------------')


def quickSortIterativeTest_randomPivot():
    quickSort_randomPivotInputs = ['q.quickSort(n_ten, 0, len(n_ten) - 1, rp)',
                                   'q.quickSort(n_hundred, 0, len(n_hundred) - 1, rp)',
                                   'q.quickSort(n_oneThousand, 0, len(n_oneThousand) - 1, rp)',
                                   'q.quickSort(n_tenThousand, 0, len(n_tenThousand) - 1, rp)',
                                   'q.quickSort(n_hundredThousand, 0, len(n_hundredThousand) - 1, rp)',
                                   'q.quickSort(n_oneMillion, 0, len(n_oneMillion) - 1, rp)']
    print()

    print(
        '***************************  Quick-Sort ( Iterative ) - randomPivot  ********************************')
    # pass the number of inputs by tweaking this len(mergeInputs)
    for x in range(0, inputsN - 1):
        quicksortTime_randomPivot = timeit.repeat(stmt=quickSort_randomPivotInputs[x], repeat=cycles,
                                                  setup=sortingSetup,
                                                  number=1)
        average = '{:.10f}'.format(sum(quicksortTime_randomPivot) / len(quicksortTime_randomPivot))
        print('Quick sort for n = ' + str(inputs[x]))
        print('Average time: %s ' % average)
        print('------------------------------------------------------------')


def binarySearchTest_nonexistent():
    """ Sort lists and then do the searching, It is done on the set up string"""

    binarySearchInputs_nonexistent = [
        'b.binary_search(sorted_numbers[0], sorted_numbers[0][0], len(sorted_numbers[0]) - 1, 20000)',
        'b.binary_search(sorted_numbers[1], sorted_numbers[1][0], len(sorted_numbers[1]) - 1, 20000)',
        'b.binary_search(sorted_numbers[2], sorted_numbers[2][0], len(sorted_numbers[2]) - 1, 20000)',
        'b.binary_search(sorted_numbers[3], sorted_numbers[3][0], len(sorted_numbers[3]) - 1, 20000)',
        'b.binary_search(sorted_numbers[4], sorted_numbers[4][0], len(sorted_numbers[4]) - 1, 20000)',
        'b.binary_search(sorted_numbers[5], sorted_numbers[5][0], len(sorted_numbers[5]) - 1, 20000)']

    print()

    print(
        '***********************  Binary search - upper bound ( Element not found ) *******************************')
    # pass the number of inputs by tweaking this len(mergeInputs)
    for x in range(0, inputsN):
        binaryTime_firstPivot = timeit.repeat(stmt=binarySearchInputs_nonexistent[x], repeat=cycles,
                                              setup=binarySetup,
                                              number=1)
        average = '{:.10f}'.format(sum(binaryTime_firstPivot) / len(binaryTime_firstPivot))
        print('Binary Search in a list of length = ' + str(inputs[x]))
        print('Average time: %s ' % average)
        print('------------------------------------------------------------')


def binarySearchTest_middleElement():
    binarySearchInputs_middleElement = [
        'b.binary_search(sorted_numbers[0], sorted_numbers[0][0], len(sorted_numbers[0]) - 1, sorted_numbers[0][(len(sorted_numbers[0]) - 1) // 2])',
        'b.binary_search(sorted_numbers[1], sorted_numbers[1][0], len(sorted_numbers[1]) - 1, sorted_numbers[1][(len(sorted_numbers[1]) - 1) // 2])',
        'b.binary_search(sorted_numbers[2], sorted_numbers[2][0], len(sorted_numbers[2]) - 1, sorted_numbers[2][(len(sorted_numbers[2]) - 1) // 2])',
        'b.binary_search(sorted_numbers[3], sorted_numbers[3][0], len(sorted_numbers[3]) - 1, sorted_numbers[3][(len(sorted_numbers[3]) - 1) // 2])',
        'b.binary_search(sorted_numbers[4], sorted_numbers[4][0], len(sorted_numbers[4]) - 1, sorted_numbers[4][(len(sorted_numbers[4]) - 1) // 2])',
        'b.binary_search(sorted_numbers[5], sorted_numbers[5][0], len(sorted_numbers[5]) - 1, sorted_numbers[5][(len(sorted_numbers[5]) - 1) // 2])']
    print()

    print(
        '***********************  Binary search - lower bound ( Element in the middle ) *****************************')
    # pass the number of inputs by tweaking this len(mergeInputs)
    for x in range(0, inputsN):
        binaryTime_middleElement = timeit.repeat(stmt=binarySearchInputs_middleElement[x], repeat=cycles,
                                                 setup=binarySetup,
                                                 number=1)
        average = '{:.10f}'.format(sum(binaryTime_middleElement) / len(binaryTime_middleElement))
        print('Binary Search in a list of length = ' + str(inputs[x]))
        print('Average time: %s ' % average)
        print('------------------------------------------------------------')


print()
print('                      ---- Performance Testing Right? ----')

# mergeSortTest()
# quickSortTest_firstPivot()
# quickSortTest_middlePivot()
# quickSortIterativeTest_randomPivot()
binarySearchTest_nonexistent()
binarySearchTest_middleElement()
# insertionSortTest()

if __name__ == '__main__':
    pass
