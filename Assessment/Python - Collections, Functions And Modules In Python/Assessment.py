import datetime

rentals = {}
late_fee = 5

def rent_book():
    name = input("Customer name: ").strip()
    title = input("Book title: ").strip()
    if not name or not title:
        print("Invalid input"); return
    if title in rentals:
        print("Book already rented"); return
    rent_date = input("Rental date (YYYY-MM-DD): ")
    due_date = input("Due date (YYYY-MM-DD): ")
    rentals[title] = {"name": name, "rent": rent_date, "due": due_date}
    print("Book rented successfully")

def return_book():
    title = input("Book title to return: ").strip()
    if title not in rentals:
        print("No such rental"); return
    data = rentals.pop(title)
    ret_date = input("Return date (YYYY-MM-DD): ")
    d1 = datetime.date.fromisoformat(data["due"])
    d2 = datetime.date.fromisoformat(ret_date)
    days_late = max(0, (d2 - d1).days)
    fee = days_late * late_fee
    print("\n----- Receipt -----")
    print("Customer:", data["name"])
    print("Book:", title)
    print("Rented on:", data["rent"])
    print("Due date:", data["due"])
    print("Returned on:", ret_date)
    print("Late days:", days_late)
    print("Late fee:", fee)
    print("-------------------\n")

def show_all():
    if not rentals:
        print("No active rentals")
    else:
        for t, d in rentals.items():
            print(f"{t} - {d['name']} (Due {d['due']})")

def main():
    while True:
        print("1 Rent book  2 Return book  3 Show rentals  4 Exit")
        c = input("Choose: ")
        if c == "1": rent_book()
        elif c == "2": return_book()
        elif c == "3": show_all()
        elif c == "4": break
        else: print("Invalid choice")

main()
