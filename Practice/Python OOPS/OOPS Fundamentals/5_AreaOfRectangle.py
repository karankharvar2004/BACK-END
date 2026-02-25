# Create a Rectangle class with method to calculate area.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        area = self.length * self.width
        return area


# Creating object
rect1 = Rectangle(10, 5)

# Calling method
print("Area of Rectangle:", rect1.calculate_area())