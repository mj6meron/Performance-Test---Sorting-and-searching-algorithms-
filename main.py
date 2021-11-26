numbersFiles = "numbers.txt"


def menu(input_number):
    my_list = []
    with open(numbersFiles, 'r') as numbers:
        for x in range(input_number):
            my_list.append(int(numbers.readline().strip('\n')))
    return my_list
