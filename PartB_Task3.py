def main():
    from random import randint
    random_num = randint(0, 256)
    if random_num < 119:
        print("It is not yet a cyclone.")
    elif random_num in range(119, 154):
        print("The storm is Category 1")
    elif random_num in range(154, 178):
        print("The storm is Category 2")
    elif random_num in range(178, 209):
        print("The storm is Category 3")
    elif random_num in range(209, 252):
        print("The storm is Category 4")
    elif random_num > 251:
        print("The storm is Category 5")
main()