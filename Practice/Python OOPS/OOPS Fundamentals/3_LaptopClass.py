# Create a Laptop class with attributes and a method display_info().

class Laptop:
    def __init__(self, brand, processor, storage):
        self.brand = brand
        self.processor = processor
        self.storage = storage 

    def display_info(self):
        print("Laptop Name:",self.brand)
        print("laptop Processor:",self.processor)
        print("Laptop Storage:",self.storage)
        print("----------------------")

thinkpad = Laptop("Lenovo","Intel i5","512-GB")
victus = Laptop("HP","Intel i7","1-TB")
ideapad = Laptop("Lenovo","Intel i3","512-GB")
iPad = Laptop("Apple","Intel-i9","1-TB")

thinkpad.display_info()