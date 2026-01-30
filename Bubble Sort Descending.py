student_scores = [78, 92, 65, 88, 71, 95, 83, 76, 89, 94]  # integer array


def bubble_sort_descending():
    temp = 0  # integer variable
    while True:
        flag = False  # boolean variable
        for count in range(len(student_scores) - 1):
            if student_scores[count] < student_scores[count + 1]:
                temp = student_scores[count]
                student_scores[count] = student_scores[count + 1]
                student_scores[count + 1] = temp
                flag = True
        if flag == False:
            break
        else:
            continue
    return student_scores


def display_array():
    print(student_scores)
    print(bubble_sort_descending())


display_array()
