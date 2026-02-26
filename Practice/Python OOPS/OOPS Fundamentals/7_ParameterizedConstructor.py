# Create a class with parameterized constructor.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


s1 = Student("Karan", 90)

print("Name:", s1.name)
print("Marks:", s1.marks)