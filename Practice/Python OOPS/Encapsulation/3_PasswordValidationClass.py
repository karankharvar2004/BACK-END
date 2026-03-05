# Create password validation class.

class PasswordManager:
    def __init__(self):
        self.__password = ""

    def set_password(self, password):
        if len(password) >= 6:
            self.__password = password
            print("Password set successfully!")
        else:
            print("Password must be at least 6 characters!")

    def check_password(self, password):
        if password == self.__password:
            print("Correct Password")
        else:
            print("Wrong Password")


pm = PasswordManager()

pm.set_password("abc123")
pm.check_password("abc123")
pm.check_password("wrong")