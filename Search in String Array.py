students = [
    "Ahmed",
    "Fatima",
    "Ali",
    "Zainab",
    "Hassan",
    "Mariam",
    "Omar",
    "Ayesha",
]  # array of string

student = input(f"Enter the student name to search: ")  # string variable


def search_student(student):
    for index in range(len(students)):
        if students[index].lower() == student.lower():
            print(index)
            break
    else:
        print(f"not found")


search_student(student)
