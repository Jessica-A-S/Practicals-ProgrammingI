def main():
    number = []
    for num in range(1, 6):
        number_entered = int(input("Please enter number {}: ".format(num)))
        number.append(number_entered)

    print(*number, sep="\n")

    number.sort()
    print("\n", *number, sep="\n")


main()
