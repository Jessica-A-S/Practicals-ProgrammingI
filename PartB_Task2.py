def main():
    from random import randint
    min_num = int(input("Please enter the smaller number: "))
    max_num = int(input("Please enter the larger number: "))
    random_num = randint(min_num, max_num)
    print(random_num)
main()