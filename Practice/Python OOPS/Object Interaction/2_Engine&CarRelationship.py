# Create Engine and Car relationship.

class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type

class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine

    def show_car(self):
        print("Car Brand:", self.brand)
        print("Engine Type:", self.engine.engine_type)

engine1 = Engine("Petrol")

car1 = Car("Toyota",engine1)
car1.show_car()