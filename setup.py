"""setUp module does the setup for the timeit module"""

sort_random = '''
import insertion_sort as i
from main import menu
import merge_sort as m
import quick_sort as q

n_ten = menu(10)
n_hundred = menu(100)
n_oneThousand = menu(1000)
n_tenThousand = menu(10000)
n_hundredThousand = menu(100000)

fp = "first element"
mp = "median of three elements"
rp = "random element"
        '''

sort_partially_sorted = '''
import insertion_sort as i
from main import menu
import merge_sort as m
import quick_sort as q

n_ten = menu(10)
n_hundred = menu(100)
n_oneThousand = menu(1000)
n_tenThousand = menu(10000)
n_hundredThousand = menu(100000)
lists = [n_ten, n_hundred, n_oneThousand, n_tenThousand, n_hundredThousand]
for e in lists:q.quickSort(e, 0, (len(e) - 1) // 2, 'middle element')

fp = "first element"
mp = "median of three elements"
rp = "random element"
        '''
sort_small_inputs = '''
import insertion_sort as i
from main import menu
import merge_sort as m
import quick_sort as q

n_5 = menu(5)
n_10 = menu(10)
n_15 = menu(15)
n_20= menu(20)
n_25 = menu(25)

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
numbers = [n_ten, n_hundred, n_oneThousand, n_tenThousand, n_hundredThousand]
sorted_numbers = []
for e in numbers: sorted_numbers.append(m.mergeSort(e))
        '''


def inputValidator(sortingAlgorithm, setup_name, smallNumberSetup):
    if setup_name == smallNumberSetup:
        if sortingAlgorithm == 'merge':
            return ['m.mergeSort(n_5)', 'm.mergeSort(n_10)', 'm.mergeSort(n_15)',
                    'm.mergeSort(n_20)', 'm.mergeSort(n_25)']
        if sortingAlgorithm == 'insertion':
            return ['i.insertion_sort(n_5)', 'i.insertion_sort(n_10)', 'i.insertion_sort(n_15)',
                    'i.insertion_sort(n_20)', 'i.insertion_sort(n_25)']
        if sortingAlgorithm == 'quick_first':
            return ['q.quickSort(n_5, 0, len(n_5) - 1, fp)',
                    'q.quickSort(n_10, 0, len(n_10) - 1, fp)',
                    'q.quickSort(n_15, 0, len(n_15) - 1, fp)',
                    'q.quickSort(n_20, 0, len(n_20) - 1, fp)',
                    'q.quickSort(n_25, 0, len(n_25) - 1, fp)']
        if sortingAlgorithm == 'quick_middle':
            return ['q.quickSort(n_5, 0, len(n_5) - 1, mp)',
                    'q.quickSort(n_10, 0, len(n_10) - 1, mp)',
                    'q.quickSort(n_15, 0, len(n_15) - 1, mp)',
                    'q.quickSort(n_20, 0, len(n_20) - 1, mp)',
                    'q.quickSort(n_25, 0, len(n_25) - 1, mp)']
        if sortingAlgorithm == 'quick_random':
            return ['q.quickSort(n_5, 0, len(n_5) - 1, rp)',
                    'q.quickSort(n_10, 0, len(n_10) - 1, rp)',
                    'q.quickSort(n_15, 0, len(n_15) - 1, rp)',
                    'q.quickSort(n_20, 0, len(n_20) - 1, rp)',
                    'q.quickSort(n_25, 0, len(n_25) - 1, rp)']
    else:
        if sortingAlgorithm == 'merge':
            return ['m.mergeSort(n_ten)', 'm.mergeSort(n_hundred)', 'm.mergeSort(n_oneThousand)',
                    'm.mergeSort(n_tenThousand)', 'm.mergeSort(n_hundredThousand)']
        if sortingAlgorithm == 'insertion':
            return ['i.insertion_sort(n_ten)', 'i.insertion_sort(n_hundred)', 'i.insertion_sort(n_oneThousand)',
                    'i.insertion_sort(n_tenThousand)', 'i.insertion_sort(n_hundredThousand)']
        if sortingAlgorithm == 'quick_first':
            return ['q.quickSort(n_ten, 0, len(n_ten) - 1, fp)',
                    'q.quickSort(n_hundred, 0, len(n_hundred) - 1, fp)',
                    'q.quickSort(n_oneThousand, 0, len(n_oneThousand) - 1, fp)',
                    'q.quickSort(n_tenThousand, 0, len(n_tenThousand) - 1, fp)',
                    'q.quickSort(n_hundredThousand, 0, len(n_hundredThousand) - 1, fp)']
        if sortingAlgorithm == 'quick_middle':
            return ['q.quickSort(n_ten, 0, len(n_ten) - 1, mp)',
                    'q.quickSort(n_hundred, 0, len(n_hundred) - 1, mp)',
                    'q.quickSort(n_oneThousand, 0, len(n_oneThousand) - 1, mp)',
                    'q.quickSort(n_tenThousand, 0, len(n_tenThousand) - 1, mp)',
                    'q.quickSort(n_hundredThousand, 0, len(n_hundredThousand) - 1, mp)']
        if sortingAlgorithm == 'quick_random':
            return ['q.quickSort(n_ten, 0, len(n_ten) - 1, rp)',
                    'q.quickSort(n_hundred, 0, len(n_hundred) - 1, rp)',
                    'q.quickSort(n_oneThousand, 0, len(n_oneThousand) - 1, rp)',
                    'q.quickSort(n_tenThousand, 0, len(n_tenThousand) - 1, rp)',
                    'q.quickSort(n_hundredThousand, 0, len(n_hundredThousand) - 1, rp)']
