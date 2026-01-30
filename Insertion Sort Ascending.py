product_prices = [
    45.99,
    23.50,
    67.80,
    12.25,
    89.99,
    34.75,
    56.20,
    78.40,
]  # integer array


def insertion_sort_ascending():
    for count in range(1, len(product_prices)):
        key = product_prices[count]  # integer variable
        index = count # integer variable
        while product_prices[index - 1] > key and index > 0:
            product_prices[index] = product_prices[index - 1]
            index -= 1
        product_prices[index] = key
    return product_prices


def display_array():
    print(product_prices)
    print(insertion_sort_ascending())


display_array()
