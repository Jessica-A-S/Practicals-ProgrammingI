from random import randint


def main():
    even = 0
    odd = 0
    for num in range(1, 101):
        random_num = randint(1, 1001)
        is_even(random_num)
        if is_even(random_num):
            even += 1
    odd = 100 - even
    print("Even:", even, "Odd:", odd)


def is_even(random_num):
    return random_num % 2 == 0


main()
