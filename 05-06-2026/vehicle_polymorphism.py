class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print(f"{self.brand} {self.model} is starting")

    def stop(self):
        print(f"{self.brand} {self.model} is stopping")


class Bike(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand, model)

    def start(self):
        print(f"Bike {self.brand} {self.model} starts with a kick or self-start")

    def stop(self):
        print(f"Bike {self.brand} {self.model} stops using brakes")


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand, model)

    def start(self):
        print(f"Car {self.brand} {self.model} starts with a key or push button")

    def stop(self):
        print(f"Car {self.brand} {self.model} stops using the brake pedal")


bike = Bike("Honda", "Shine")
car = Car("Toyota", "Innova")

vehicles = [bike, car]

for vehicle in vehicles:
    vehicle.start()
    vehicle.stop()
