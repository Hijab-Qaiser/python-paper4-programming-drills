test_scores = [45, 67, 89, 34, 78, 92, 56, 88, 71, 95]  # integer array


def find_grade_range(min, max):
    occured = []  # emty array of integers

    for count in range(len(test_scores)):
        if test_scores[count] >= min and test_scores[count] <= max:
            occured.append((test_scores[count]))

    if len(occured) == 0:
        print(f"None")
    else:
        print(occured)


while True:
    min = int(input(f"Enter minimum range "))  # integer variable
    max = int(input(f"Enter maximum range "))  # integer variable
    if min >= 0 and min <= 100 and max >= 0 and max <= 100:
        break
    else:
        continue


find_grade_range(min, max)
