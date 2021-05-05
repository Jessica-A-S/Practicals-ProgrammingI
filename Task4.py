def main():
    price = float(input("Enter original price: "))
    percentage = float(input("Enter the discount percentage in decimal form: "))
    calc_discount_price(price, percentage)
    print("The discounted price is $", calc_discount_price(price, percentage))


def calc_discount_price(price, percentage):
    discount = price * percentage
    discount_price = price - discount
    return discount_price


main()
