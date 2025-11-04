# RentTrack - Basic Book Rental System (Module 13)

# Function to rent a book
def rent_book():
    print("\n--- Book Rental ---")
    customer = input("Enter customer name: ")
    book = input("Enter book title: ")
    rent_date = input("Enter rental date (DD-MM-YYYY): ")
    return_date = input("Enter expected return date (DD-MM-YYYY): ")

    print("\nBook rented successfully!")
    print("Customer:", customer)
    print("Book Title:", book)
    print("Rental Date:", rent_date)
    print("Return Date:", return_date)


# Function to return a book
def return_book():
    print("\n--- Book Return ---")
    customer = input("Enter customer name: ")
    book = input("Enter book title: ")
    due_date = int(input("Enter due day number (e.g., 10 for 10th): "))
    return_day = int(input("Enter actual return day number: "))

    if return_day > due_date:
        late_days = return_day - due_date
        late_fee = late_days * 10  # ₹10 per day
        print("\nBook returned late!")
        print("Late Days:", late_days)
        print("Late Fee: ₹", late_fee)
    else:
        print("\nBook returned on time. No late fee.")

    print("\nReturn Summary:")
    print("Customer:", customer)
    print("Book Title:", book)
    print("Returned Successfully!")


# Main program loop
while True:
    print("\n==== RentTrack Library System ====")
    print("1. Rent a Book")
    print("2. Return a Book")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        rent_book()
    elif choice == "2":
        return_book()
    elif choice == "3":
        print("\nThank you for using RentTrack!")
        break
    else:
        print("Invalid choice. Please try again.")
