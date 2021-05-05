def main():
    num_1 = int(input("Enter first number: "))
    num_2 = int(input("Enter second number: "))
    max_num(num_1, num_2)
    print("The larger number of {} and {} is {}.".format(num_1, num_2, max_num(num_1, num_2)))


def max_num(num_1, num_2):
    if num_1 > num_2:
        greater_num = num_1
    elif num_2 > num_1:
        greater_num = num_2
    else:
        greater_num = "the same"
    return greater_num


main()
