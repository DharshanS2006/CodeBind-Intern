class Person:
    def show_person(self):
        print("This is a person.")


class Employee(Person):
    def show_employee(self):
        print("This person is an employee.")


class Manager(Employee):
    def show_manager(self):
        print("This employee is a manager.")


manager = Manager()
manager.show_person()
manager.show_employee()
manager.show_manager()
