# Create a class where attributes are private.

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private variable

    def show_balance(self):
        print("Balance:", self.__balance)


account1 = BankAccount(1000)
account1.show_balance()

# print(account1.__balance)  ❌ This will give error