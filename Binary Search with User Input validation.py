ages = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]  # integer array

while True:
    while True:
        value = int(input(f"Enter a valid age: "))  # integer variable
        if value < 18 or value > 30:
            continue
        else:
            break

    def binary_search(ages, value):
        UB = len(ages) - 1  # integer variable
        LB = 0  # integer variable

        while LB <= UB:
            MP = int((UB + LB) / 2)  # integer variable
            if ages[MP] == value:
                return f"Found at {MP} index "
            elif value > ages[MP]:
                LB = MP + 1
            else:
                UB = MP - 1
        return f"Not found "

    print(binary_search(ages, value))
    end = input(f"Do you want to continue searching? ")  # string variable
    if end == "yes":
        continue
    else:
        break
