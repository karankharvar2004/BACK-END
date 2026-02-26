# Create a Student class with name and marks.

class Student:
    def __init__(self, name, marks): 
        self.name = name
        self.marks = marks

#Creating Objects
student1 = Student("Karan",85)

print("Name:",student1.name)
print("Marks:",student1.marks)