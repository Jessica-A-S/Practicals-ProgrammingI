def main():
    course = {"CS101": ("Room: 3004", "Instructor: Haynes", "Time: 8:00 a.m."),
              "CS102": ("Room: 4501", "Instructor: Alvarado", "Time: 9:00 a.m."),
              "CS103": ("Room: 6755", "Instructor: Rich", "Time: 10:00 a.m."),
              "NT110": ("Room: 1244", "Instructor: Burke", "Time: 11:00 a.m."),
              "CM241": ("Room: 1411", "Instructor: Lee", "Time: 1:00 p.m.")}

    student_code = input("Input your subject code: ")

    if student_code == "CS101":
        print(course["CS101"])
    elif student_code == "CS102":
        print(course["CS102"])
    elif student_code == "CS103":
        print(course["CS103"])
    elif student_code == "NT110":
        print(course["NT110"])
    elif student_code == "CM241":
        print(course["CM241"])
    else:
        print("Wrong course number")


main()
