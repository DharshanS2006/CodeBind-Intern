class Animal:
    def eat(self):
        print("Animal eats food.")


class Dog(Animal):
    def bark(self):
        print("Dog barks.")


dog = Dog()
dog.eat()
dog.bark()
