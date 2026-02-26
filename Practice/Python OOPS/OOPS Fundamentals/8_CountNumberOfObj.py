# Create a class that counts number of objects created.

class Car:
    count = 0   # class variable

    def __init__(self, brand):
        self.brand = brand
        Car.count += 1


c1 = Car("BMW")
c2 = Car("Audi")
c3 = Car("Tesla")

print("Total Objects Created:", Car.count)