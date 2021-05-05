def main():
    students = int(input("How many students do you have? "))
    test_scores = int(input("How many test scores per student? "))

    test_total = 0
    test_num = 0

    for student_num in range(1, students + 1):
        print("Student number {}".format(student_num))
        print("----------------")
        for test_num in range(1, test_scores + 1):
            test = int(input("Enter test {}".format(test_num)))
            test_total += test
        test_average = test_total / test_num
        print("The average for Student number {} is {}".format(student_num, test_average))
        test_total = 0


main()
