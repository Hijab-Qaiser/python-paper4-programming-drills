daily_temps = [28, 32, 25, 30, 27, 33, 26, 29, 31, 24]  # integer array


def insertion_sort_descending(daily_temps):
    for count in range(1, len(daily_temps)):
        key = daily_temps[count]  # integer variable
        index = count  #  integer variable
        while index > 0 and daily_temps[index - 1] < key:
            daily_temps[index - 1] = daily_temps[index]
            index -= 1
        daily_temps[index] = key
    return daily_temps


def show_temperatures():
    print(daily_temps)
    insertion_sort_descending(daily_temps)
    for count in range(len(daily_temps)):
        print(f"{daily_temps[count]}°C")


show_temperatures()
