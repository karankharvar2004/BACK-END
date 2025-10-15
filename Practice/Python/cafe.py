# cafe.py

def menu():
    print("Srno.  Category")
    print("1.     Beverages")
    print("2.     Snacks")
    print("3.     Desserts")

def line():
    print("=" * 67)

def beverage_choice():
    x = int(input("Enter Choice: "))
    tea_price = 50
    coffee_price = 70
    juice_price = 90

    if x == 1:
        print("Selected Tea")
        line()
        qty = int(input("Enter Quantity: "))
        line()
        total = tea_price * qty
        print("Total:", total)
        line()
        return total
    elif x == 2:
        print("Selected Coffee")
        line()
        qty = int(input("Enter Quantity: "))
        line()
        total = coffee_price * qty
        print("Total:", total)
        line()
        return total
    elif x == 3:
        print("Selected Fresh Juice")
        line()
        qty = int(input("Enter Quantity: "))
        line()
        total = juice_price * qty
        print("Total:", total)
        line()
        return total
    else:
        print("Invalid Choice")
        line()
        return 0

def snack_choice():
    x = int(input("Enter Choice: "))
    sandwich_price = 80
    burger_price = 120
    fries_price = 60

    if x == 1:
        print("Selected Sandwich")
        line()
        qty = int(input("Enter Quantity: "))
        line()
        total = sandwich_price * qty
        print("Total:", total)
        line()
        return total
    elif x == 2:
        print("Selected Burger")
        line()
        qty = int(input("Enter Quantity: "))
        line()
        total = burger_price * qty
        print("Total:", total)
        line()
        return total
    elif x == 3:
        print("Selected Fries")
        line()
        qty = int(input("Enter Quantity: "))
        line()
        total = fries_price * qty
        print("Total:", total)
        line()
        return total
    else:
        print("Invalid Choice")
        line()
        return 0

def dessert_choice():
    x = int(input("Enter Choice: "))
    cake_price = 100
    icecream_price = 90
    brownie_price = 120

    if x == 1:
        print("Selected Cake Slice")
        line()
        qty = int(input("Enter Quantity: "))
        line()
        total = cake_price * qty
        print("Total:", total)
        line()
        return total
    elif x == 2:
        print("Selected Ice Cream")
        line()
        qty = int(input("Enter Quantity: "))
        line()
        total = icecream_price * qty
        print("Total:", total)
        line()
        return total
    elif x == 3:
        print("Selected Brownie")
        line()
        qty = int(input("Enter Quantity: "))
        line()
        total = brownie_price * qty
        print("Total:", total)
        line()
        return total
    else:
        print("Invalid Choice")
        line()
        return 0

def beverages():
    line()
    print("Srno.  Item          Price")
    print("1.     Tea           50")
    print("2.     Coffee        70")
    print("3.     Fresh Juice   90")
    line()
    return beverage_choice()

def snacks():
    line()
    print("Srno.  Item          Price")
    print("1.     Sandwich      80")
    print("2.     Burger        120")
    print("3.     Fries         60")
    line()
    return snack_choice()

def desserts():
    line()
    print("Srno.  Item          Price")
    print("1.     Cake Slice    100")
    print("2.     Ice Cream     90")
    print("3.     Brownie       120")
    line()
    return dessert_choice()
