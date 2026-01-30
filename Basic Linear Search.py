numbers = [45, 23, 67, 12, 89, 34, 56, 78, 91, 25]  # array of integers


def linear_search(search):
    for count in range(len(numbers)):
        if numbers[count] == search:
            return True
            break
    return False


search = int(input(f"Enter an element to search "))  # integer variable
print(linear_search(search))
