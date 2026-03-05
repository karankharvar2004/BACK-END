# Create ATM machine simulation.

class ATM:
    def __init__(self, balance):
        self.__balance = balance

    def check_balance(self):
        print("Current Balance:", self.__balance)

    def deposit(self, amount):
        self.__balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient Balance!")


atm1 = ATM(1000)

atm1.check_balance()
atm1.deposit(500)
atm1.withdraw(300)
atm1.withdraw(2000)
atm1.check_balance()