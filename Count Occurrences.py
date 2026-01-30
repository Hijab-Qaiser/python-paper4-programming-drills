scores = [85, 92, 78, 85, 90, 85, 76, 88, 85, 94]  # array of integers


def count_occurrences(search):
    occur = 0  # int variable
    for count in range(len(scores)):
        if scores[count] == search:
            occur += 1
    return occur


search = int(input(f"Enter an element to search "))  # integer variable
print(count_occurrences(search))
