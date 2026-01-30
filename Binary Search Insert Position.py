employee_ids = [
    1012,
    1025,
    1038,
    1041,
    1055,
    1069,
    1072,
    1086,
    1099,
    1105,
]  # integer array

id = int(input(f"Enter an employee id to search "))  # integer variable


def binary_search_insert(id):
    index = 0  # integer variable
    UB = len(employee_ids) - 1  # integer variable
    LB = 0  # integer variable

    while LB <= UB:
        MP = int((LB + UB) / 2)  # integer variable

        if employee_ids[MP] == id:
            return f"ID already exists "
        elif id < employee_ids[MP]:
            UB = MP - 1
        else:
            LB = MP + 1
    employee_ids.append(id)
    temp = 0  # integer variable
    while True:
        flag = False  # boolean variable
        for count in range(len(employee_ids) - 1):
            if employee_ids[count] > employee_ids[count + 1]:
                temp = employee_ids[count]
                employee_ids[count] = employee_ids[count + 1]
                employee_ids[count + 1] = temp
                flag = True
        if flag == False:
            break
        else:
            continue
    for count in range(len(employee_ids)):
        if id == employee_ids[count]:
            index = count
            break

    return f"ID inserted at position {index} "


print(binary_search_insert(id))
