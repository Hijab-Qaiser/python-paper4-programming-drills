product_ids = [
    1001,
    1005,
    1003,
    1005,
    1007,
    1005,
    1002,
    1008,
    1005,
    1004,
]  # array of integers
occur = []  # empty integer array to store all indexes where ID found


def find_all_positions(search_id):
    for count in range(len(product_ids)):
        if product_ids[count] == search_id:
            occur.append(count)
    if len(occur) == 0:
        return -1
    else:
        return occur


search_id = int(input(f"Enter a product id to search "))  # integer variable
print(find_all_positions(search_id))
