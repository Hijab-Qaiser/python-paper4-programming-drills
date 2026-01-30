employees = [  # Sorted by EmployeeID
    [1001, 45000],
    [1005, 52000],
    [1012, 48000],
    [1023, 67000],
    [1034, 55000],
    [1045, 71000],
    [1056, 49000],
    [1067, 63000],
]  # 2d array of integers

id = int(input(f"Enter an element to search: "))  # integer variable


def binary_search_employee(id):
    UB = len(employees) - 1  # integer variable
    LB = 0  # integer variable

    while LB <= UB:
        MP = int((LB + UB) / 2) # integer variable

        if employees[MP][0] == id:
            return MP
        elif id < employees[MP][0]:
            UB = MP - 1
        else:
            LB = MP + 1
    return -1


def display_employee_salary(employees, emp_id):
    if emp_id == -1:
        print(f"Not Found ")
    else:
        print(f"Salary Of Employee {employees[emp_id][0]} is {employees[emp_id][1]} ")


display_employee_salary(employees, binary_search_employee(id))
