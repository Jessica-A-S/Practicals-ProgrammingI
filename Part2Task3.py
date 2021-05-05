def main():
    correct = 0
    incorrect = 0
    state_caps = {
        "QLD": "Brisbane",
        "NSW": "Sydney",
        "VIC": "Melbourne",
        "SA": "Adelaide",
        "WA": "Perth",
        "TAS": "Hobart",
        "NT": "Darwin"}
    choice = input("P = Play, Q = Quit ").upper()
    while choice == "P":
        for state in state_caps:
            question = input("What is the capital of {}? ".format(state))
            if question == state_caps:
                correct += 1
            else:
                incorrect += 1
        print("You got {} correct and {} incorrect".format(correct, incorrect))
        choice = input("P = Play, Q = Quit").upper()
    if choice == "Q":
        print("Thanks for playing.")


def confirm_answer(question, state_caps):
    correct = []
    incorrect = []
    if question == state_caps:
        print("Correct")
        correct += 1
    else:
        print("Incorrect")
        incorrect += 1
    return


main()