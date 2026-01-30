student_marks = [67, 82, 91, 45, 88, 73, 56, 94, 79, 85]  # array of integers


def linear_search(mark):
    for count in range(len(student_marks)):
        if student_marks[count] == mark:
            print(count)
            break
    else:
        print(f"not found")


mark = int(input(f"Enter marks to search "))  # integer variable
while True:
    if mark < 0 or mark > 100:
        mark = int(input(f"Please enter valid marks "))
        continue
    else:
        break

linear_search(mark)
