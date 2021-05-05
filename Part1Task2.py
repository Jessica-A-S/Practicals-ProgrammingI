def main():
    tests = []
    for num in range(1, 6):
        test = int(input("Enter test score: "))
        tests.append(test)
    for test in tests:
        determine_grade(test)
        print(determine_grade(test))
    calc_average(tests)
    print(calc_average(tests))


def determine_grade(test):
    if test >= 85:
        grade = "HD"
    elif test >= 75:
        grade = "D"
    elif test >= 65:
        grade = "C"
    elif test >= 50:
        grade = "P"
    else:
        grade = "F"
    return grade


def calc_average(tests):
    avg = sum(tests) / 5
    return avg


main()
