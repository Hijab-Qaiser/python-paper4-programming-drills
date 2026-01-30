# Monthly sales figures in thousands
monthly_sales = [
    245,
    312,
    289,
    356,
    298,
    334,
    267,
    389,
    412,
    378,
    295,
    401,
]  # integers array

while True:
    target = int(input(f"Enter a valid monthly sales "))  # integer variable
    if target > 0:
        break
    else:
        continue


def analyze_sales(target):
    occur = 0  # integer variable
    sum = 0  # integer
    flag = False  # boolean variable
    for count in range(len(monthly_sales)):
        if monthly_sales[count] == target:
            flag = True
            occur += 1
        sum = sum + monthly_sales[count]
    average = sum / (len(monthly_sales))
    if flag == True:
        print(f"Sales figure {target} found ")
        print(f"Occurrences: {occur} ")
        print(f"Array average: {average} ")
        if target > average:
            print(f"Target is above average ")
        elif target < average:
            print(f"Target is below average ")
        else:
            print(f"Target and average are equal ")
    else:
        print(f"Sales figure not found")


analyze_sales(target)
