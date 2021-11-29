""" This main file does all the performance testing"""

numbersFiles = "numbers.txt"


def menu(input_number):
    my_list = []
    with open(numbersFiles, 'r') as numbers:
        for x in range(input_number):
            my_list.append(int(numbers.readline().strip('\n')))
    return my_list

# def insertionSortTest1():
#     for x in range(0, 5):
#         start = time.time()
#         i.insertion_sort(n_tenThousand)
#         end = time.time()
#         print('Time: ' + str(end - start))
#         print('------------------')
#         insertionSortRunningTime.append(end - start)
#         # print(insertionSortRunningTime)
#     average = sum(insertionSortRunningTime) / 5
#     print('Average : ' + str(average))


# mergeSortRunningTime = []
# insertionSortRunningTime = []
# quicksortRunningTime_firstPivot = []
# quicksortRunningTime_medianPivot = []
# quicksortRunningTime_randomPivot = []
# binarySearchRunningTime = []
