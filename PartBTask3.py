def main():
    age = int(input("Enter your age: "))
    enrolled = input("Are you enrolled to vote(Y/N)? ").upper()
    if age >= 18:
        age = True
        if enrolled == "Y":
            enrolled = True
        else:
            enrolled = False
    else:
        enrolled = False
    if age and enrolled:
        print("You are enrolled to vote")
    else:
        print("You are not eligible to vote")


main()
