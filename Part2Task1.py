def main():
    tuple_list = (54, 76, 32, 14, 29, 12, 64, 97, 50, 86, 43, 12)

    menu = input("1-Display minimum \n2-Display maximum \n3-Display total \n4-Display average \n5-Quit \n")
    if menu != ("1", "2", "3", "4", "5"):
        print("Invalid choice")
        menu = input("1-Display minimum \n2-Display maximum \n3-Display total \n4-Display average \n5-Quit \n")

    while menu != "5":
        if menu == "1":
            print(min(tuple_list))
        elif menu == "2":
            print(max(tuple_list))
        elif menu == "3":
            print(sum(tuple_list))
        elif menu == "4":
            print(sum(tuple_list) / 12)
        menu = input("1-Display minimum \n2-Display maximum \n3-Display total \n4-Display average \n5-Quit \n")
    if menu == "5":
        print("Goodbye")


main()
