def main():
    value = int(input("Enter a value. "))
    ten_percent(value)
    print("10 percent of", value, "is", ten_percent(value))


def ten_percent(value):
    result = value * 0.1
    return result


main()
