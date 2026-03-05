# Create a class that prevents negative balance.

class BankAccount:
    def __init__(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            self.__balance = 0
            print("Initial Balance Cannot be Negative!!")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit must be Positive!!")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Cannot Withdraw!! Balance Would go Negative!!")
        else:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance
    
account1 = BankAccount(1000)
account1.withdraw(1200)
print("Balance:",account1.get_balance()) 