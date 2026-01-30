student_ids = [
    1001,
    1005,
    1012,
    1023,
    1034,
    1045,
    1056,
    1067,
    1078,
    1089,
    1095,
    1102,
]  # integer array

student_id = int(input(f"Enter a student ID to search "))


def binary_search_step(student_id):
    UB = len(student_ids) - 1  # integer variable
    LB = 0  # integer variable
    count = 0  # integer variable
    flag = False  # boolean variable

    while LB <= UB:
        MP = int((UB + LB) / 2)  # integer variable

        if student_ids[MP] == student_id:
            count += 1
            print(f"ID found at index {MP} after {count} comparisons")
            flag = True
            break
        elif student_id < student_ids[MP]:
            UB = MP - 1
            count += 1
        else:
            LB = MP + 1
            count += 1
    if flag == False:
        print(f"ID not found after {count} comparisons")


binary_search_step(student_id)
