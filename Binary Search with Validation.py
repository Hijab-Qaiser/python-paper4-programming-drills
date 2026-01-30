exam_scores = [23, 34, 45, 52, 61, 67, 73, 78, 82, 87, 91, 95]  # integer array

while True:
    value = int(input(f"Enter valid marks to search "))  # integer value
    if value < 0 or value > 100:
        continue
    else:
        break


def search_score(exam_scores, value):
    UB = len(exam_scores) - 1  # integer variable
    LB = 0  # integer variable

    while LB < UB:
        MP = int((UB + LB) / 2)  # integer variable

        if exam_scores[MP] == value:
            return f"Found at {MP} index "

        elif value < exam_scores[MP]:
            UB = MP - 1
        else:
            LB = MP + 1
    return -1


print(search_score(exam_scores, value))
