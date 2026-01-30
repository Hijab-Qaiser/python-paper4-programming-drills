unsorted_array = [64, 34, 25, 12, 22, 11, 90, 88, 45, 50]  # integer array


def bubble_sort_ascending():
    temp = 0  # integer variable
    while True:
        flag = False  # boolean variable
        for count in range(len(unsorted_array) - 1):
            if unsorted_array[count] > unsorted_array[count + 1]:
                temp = unsorted_array[count]
                unsorted_array[count] = unsorted_array[count + 1]
                unsorted_array[count + 1] = temp
                flag = True
        if flag == False:
            break
        else:
            continue
    return unsorted_array


def display_array():
    print(unsorted_array)
    print(bubble_sort_ascending())


display_array()
