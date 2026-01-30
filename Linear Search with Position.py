numbers = [45, 23, 67, 12, 89, 34, 56, 78, 91, 25]  # array of ntegers


def find_position(search):
    for count in range(len(numbers)):
        if numbers[count] == search:
            return count
            break
    return -1


search = int(input(f"Enter an element to search "))  # integer variable
print(find_position(search))
