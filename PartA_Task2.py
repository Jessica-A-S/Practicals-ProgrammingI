def main():
    age = int(input("What is your age? "))
    enrolled = input("Are you enrolled to vote? ")
    if age >= 18 and enrolled == "yes":
        print("Go Vote!")
    elif age >= 18 and enrolled == "no":
        print("You are old enough to vote, but are not enrolled.")
    elif age < 18 and enrolled == "yes":
        print("You are not yet 18 but you are enrolled.")
    elif age < 18 and enrolled == "no":
        print("Go home kid.")
main()