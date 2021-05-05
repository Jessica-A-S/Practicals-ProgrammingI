def main():
    age = int(input("What is your age? "))
    while not 0 < age < 130:
        print("That age is invalid")
        age = int(input("What is your age? "))
    print("Age accepted. Have a nice day.")
main()