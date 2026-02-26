# Create a class with class variable and instance variable difference.

class Employee:
    company_name = "Google"   # class variable

    def __init__(self, name):
        self.name = name      # instance variable


e1 = Employee("Karan")
e2 = Employee("Rahul")

print("Company:", e1.company_name)
print("Employee 1:", e1.name)
print("Employee 2:", e2.name)