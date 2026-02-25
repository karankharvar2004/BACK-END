# Create a BankAccount class with deposit and withdraw methods.

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount Deposited:", amount)
        print("Updated Balance:", self.balance)
        print("----------------------")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount Withdrawn:", amount)
            print("Updated Balance:", self.balance)
        else:
            print("Insufficient Balance!")
        print("----------------------")


# Creating object
account1 = BankAccount("Karan", 1000)

# Testing methods
account1.deposit(500)
account1.withdraw(300)
account1.withdraw(2000)
