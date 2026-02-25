# Create a Car class with brand and price.

class Car:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def display_info(self):
        print("Car Name:", self.brand)
        print("Car Price:", self.price)

nano_car = Car("TATA", 200000)
suzuki_car = Car("Maruti Suzuki", 500000)
porsche_car = Car("Lamborghini", 900000)

nano_car.display_info()
suzuki_car.display_info()
porsche_car.display_info()