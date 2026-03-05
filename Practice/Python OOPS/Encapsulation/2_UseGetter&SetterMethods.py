# Use getter and setter methods.

class Person:
    def __init__(self, age):
        self.__age = age   # private variable

    # Getter method
    def get_age(self):
        return self.__age

    # Setter method
    def set_age(self, new_age):
        if new_age > 0:
            self.__age = new_age
        else:
            print("Age must be positive!")


p1 = Person(21)

print("Age:", p1.get_age())

p1.set_age(25)
print("Updated Age:", p1.get_age())