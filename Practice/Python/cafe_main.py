import cafe

total = 0

def line():
    print("*" * 67)

while True:
    line()
    print("Welcome to Mocha Café ☕")
    line()
    cafe.menu()
    line()

    choice = int(input("Enter Category Choice: "))

    if choice == 1:
        total += cafe.beverages()
    elif choice == 2:
        total += cafe.snacks()
    elif choice == 3:
        total += cafe.desserts()
    else:
        print("Invalid Category Choice")

    print("Do you want to order anything else?")
    line()
    print("Yes => 1   |   No => 2")
    line()
    more = int(input("Enter Choice: "))
    line()

    if more == 1:
        continue
    elif more == 2:
        name = input("Enter Your Name: ")
        line()
        number = input("Enter Your Mobile Number: ")
        line()
        print("Total Bill Amount: ₹", total)
        print("Thank You,", name)
        print("Contact Number:", number)
        print("Visit Again ☕❤️")
        line()
        break
