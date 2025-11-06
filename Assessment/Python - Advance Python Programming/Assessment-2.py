from datetime import datetime

rentals = []

def rent_book():
    print("\n--- Book Rental ---")
    customer = input("Enter customer name: ")
    book = input("Enter book title: ")
    rent_date = input("Enter rental date (DD-MM-YYYY): ")
    return_date = input("Enter expected return date (DD-MM-YYYY): ")

    rental = {
        "customer": customer,
        "book": book,
        "rent_date": rent_date,
        "return_date": return_date
    }

    rentals.append(rental)
    print("\nBook rented successfully!")
    print("Customer:", customer)
    print("Book:", book)
    print("Rental Date:", rent_date)
    print("Return Date:", return_date)


def return_book():
    print("\n--- Book Return ---")
    customer = input("Enter customer name: ")
    book = input("Enter book title: ")
    actual_return = input("Enter actual return date (DD-MM-YYYY): ")

    found = False
    for rental in rentals:
        if rental["customer"] == customer and rental["book"] == book:
            found = True
            expected_date = datetime.strptime(rental["return_date"], "%d-%m-%Y")
            actual_date = datetime.strptime(actual_return, "%d-%m-%Y")

            days_late = (actual_date - expected_date).days

            if days_late > 0:
                late_fee = days_late * 10 
                print(f"\nBook returned late by {days_late} days.")
                print(f"Late Fee: ₹{late_fee}")
            else:
                print("\nBook returned on time. No late fee.")

            print("\n--- Return Summary ---")
            print("Customer:", customer)
            print("Book:", book)
            print("Expected Return:", rental["return_date"])
            print("Actual Return:", actual_return)
            break

    if not found:
        print("\nNo rental record found for that customer or book.")


def show_rentals():
    if len(rentals) == 0:
        print("\nNo rentals recorded yet.")
    else:
        print("\n--- Current Rentals ---")
        for r in rentals:
            print(f"Customer: {r['customer']} | Book: {r['book']} | Rent Date: {r['rent_date']} | Return Date: {r['return_date']}")


while True:
    print("\n==== RentTrack Library System ====")
    print("1. Rent a Book")
    print("2. Return a Book")
    print("3. View All Rentals")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        rent_book()
    elif choice == "2":
        return_book()
    elif choice == "3":
        show_rentals()
    elif choice == "4":
        print("\nThank you for using RentTrack!")
        break
    else:
        print("Invalid choice. Please try again.")
