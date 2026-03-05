# Create a Person class with private salary.

class Person:
    def __init__(self, salary):
        self.__salary = salary     # private variable

    def person_salary(self):
        print("Salary:", self.__salary)

person1 = Person("25000rs")
person1.person_salary()

# print(person1._salary) ❌ This will give error