def main():
    years = int(input("How many years? "))
    total_rainfall = 0
    months = 0
    for num_year in range(1, years + 1):
        print("Year {}:".format(num_year))
        for months in range(1, 13):
            monthly_rainfall = int(input("Inches of rainfall for month {} ? ".format(months)))
            total_rainfall += monthly_rainfall
        average_rainfall = total_rainfall / months
        print("For {} months, the total rainfall is {} inches.".format(months, total_rainfall))
        print("The average rainfall for {} months is {:.2f} inches.".format(months, average_rainfall))


main()
