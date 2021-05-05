GRAVITY = 9.8


def main():
    for time in range(1, 11):
        falling_distance(time)
        print(time, "sec is", format(falling_distance(time), ',.1f'), "metres")


def falling_distance(time):
    distance = 0.5 * GRAVITY * (time ** 2)
    return distance


main()
