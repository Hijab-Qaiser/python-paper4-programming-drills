data_array = [
    5,
    12,
    18,
    24,
    31,
    37,
    43,
    49,
    55,
    62,
    68,
    74,
    80,
    86,
    92,
    98,
    104,
    110,
    116,
    122,
]  # integer array

value = int(input(f"Enter a value to search "))  # integer variable


def linear_search_count(data_array, value):
    flag = False  # boolean variable
    index = 0  # integer variable
    for count in range(len(data_array)):
        if data_array[count] == value:
            flag = True
            print(f"found at {count} position after {index} iterations ")
            break
        else:
            index += 1
    if flag == False:
        print(f"not found ")


def binary_search_count(data_array, value):
    flag = False  # boolean variable
    UB = len(data_array) - 1  # integer variable
    LB = 0  # integer variable
    count = 1  # integer variable

    while LB <= UB:
        MP = int((UB + LB) / 2)  # integer variable
        if data_array[MP] == value:
            count += 1
            flag = True
            print(f"found at {MP} position after {count} iterations ")
            break
        elif value < data_array[MP]:
            UB = MP - 1
            count += 1
        else:
            LB = MP + 1
            count += 1
    if flag == False:
        print(f"not found ")


linear_search_count(data_array, value)
binary_search_count(data_array, value)
