sorted_numbers = [12, 23, 34, 45, 56, 67, 78, 89, 101, 112]  # integer array


value = int(input(f"Enter an element to search "))  # integer variable


def binary_search(value):
    UB = len(sorted_numbers) - 1  # integer variable
    LB = 0  # integer variable

    while LB <= UB:
        MP = int((UB + LB) / 2)  # integer variable

        if sorted_numbers[MP] == value:
            return True
        elif value < sorted_numbers[MP]:
            UB = MP - 1
        else:
            LB = MP + 1
    return False


print(binary_search(value))
