class Vehicle:
    def start(self):
        print("Vehicle starts.")


class Car(Vehicle):
    def drive_car(self):
        print("Car is driving.")


class Bike(Vehicle):
    def ride_bike(self):
        print("Bike is riding.")


car = Car()
car.start()
car.drive_car()

bike = Bike()
bike.start()
bike.ride_bike()
