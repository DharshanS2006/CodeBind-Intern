class Bird:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} says: Chirp chirp")


class Cat:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} says: Meow meow")


bird = Bird("Parrot")
cat = Cat("Kitty")

animals = [bird, cat]

for animal in animals:
    animal.sound()
