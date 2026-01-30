prices = [
    15.99,
    22.50,
    28.75,
    34.20,
    41.00,
    48.99,
    55.50,
    63.25,
    71.80,
    79.95,
]  # integer array


while True:
    min_price = float(input(f"Enter a valid minimum price: "))  # float variable
    max_price = float(input(f"Enter a valid maximum price: "))  # float variable
    if min_price < 0.0 or max_price > 100.0:
        continue
    else:
        break


def find_price_range(min_price, max_price):
    result = []  # empty float array
    start = 0  # integer variable
    end = 0  # integer variable
    
    UB = len(prices) - 1  # integer variable
    LB = 0  # integer variable
    while LB <= UB:

        MP = int((UB + LB) / 2)  # integer variable
        if prices[MP] >= min_price:
            UB = MP - 1
        else:
            LB = MP + 1
    start = LB

    UB = len(prices) - 1  # integer variable
    LB = 0  # integer variable
    while LB <= UB:

        MP = int((UB + LB) / 2)  # integer variable
        if prices[MP] <= max_price:
            LB = MP + 1
        else:
            UB = MP - 1
    end = UB
    if start > end:
        return f"No range exist "
    else:
        for count in range(start, end + 1, 1):
            result.append(prices[count])

    return result


print(find_price_range(min_price, max_price))
