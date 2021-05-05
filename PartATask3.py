def main():
    MAX_SETS = 5
    MAX_NUMBERS = 2

    total_sum = 0
    total = 0

    for set_number in range(1, MAX_SETS + 1):
        for number in range(1, MAX_NUMBERS + 1):
            value = int(input("Enter number {} of set {}:".format(number, set_number)))
            total_sum += value
        print("The sum of set {} is {}.".format(set_number, total_sum))
        total = total + total_sum
        total_sum = 0

    print("The total of all the sets is {}.".format(total))


main()
