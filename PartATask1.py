def main():
    finished = False

    while not finished:
        value = int(input("Enter a value to be cubed. "))
        cube = value ** 3
        print(value, "cubed is", cube)
        choice = input("Cube another number? ")
        if choice == "no":
            finished = True
            print("Goodbye")


main()
