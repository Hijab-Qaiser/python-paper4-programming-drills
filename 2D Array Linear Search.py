student_results = [
    [78, 82, 75],  # Student 0: Math, Science, English
    [65, 70, 68],  # Student 1
    [92, 88, 90],  # Student 2
    [56, 60, 58],  # Student 3
    [85, 78, 82],  # Student 4
]  # 2d array of integers


def search_in_2d_array(score):
    for row in range(5):
        for column in range(3):
            if student_results[row][column] == score:
                return row, column
    return -1, -1


score = int(input(f"Enter a subject marks to search: "))  # integer variable
student_index, subject_index = search_in_2d_array(score)  # integer variables
if student_index == -1:
    print("Score not found ")
else:
    match subject_index:
        case 0:
            subject_index = "Math"
        case 1:
            subject_index = "Science"
        case 2:
            subject_index = "English"
    print(f"Student {student_index}, Subject {subject_index} scored {score}")
