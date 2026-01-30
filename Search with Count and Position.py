temperatures = [28, 32, 28, 30, 28, 31, 28, 29, 33, 28]  # array of integers

temp = int(input(f"Enter the target temperature "))  # integer variable


def temp_search(temp):
    total = 0  # integer variable
    for count in range(len(temperatures)):
        if temperatures[count] == temp:
            total += 1
    for count in range(len(temperatures)):
        if temperatures[count] == temp:
            first_pos = count  # integer variable
            break
    print(
        f"Temperature {temp}°C appeared {total} times, first occurrence at index {first_pos}"
    )


temp_search(temp)
