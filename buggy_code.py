def average_list():
    '''
    this function Gets two lists, concatenates them, and calculates the average of the total list
    :return: None
    '''
    list1 = [2, 4, 6, 8]
    list2 = [10, 20, 30, 40]
    the_list = list1 + list2
    sum = 0
    amount = 0
    for number in the_list:
        sum += number
        amount += 1
    average = sum / amount
    print(f"the average is {average}")


def main():
    average_list()

if __name__ == '__main__':
    main()