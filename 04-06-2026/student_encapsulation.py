class Student:
    def __init__(self, name, roll_number, marks):
        self.__name = name
        self.__roll_number = roll_number
        self.__marks = marks

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_roll_number(self):
        return self.__roll_number

    def set_roll_number(self, roll_number):
        self.__roll_number = roll_number

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        self.__marks = marks

    def display_details(self):
        print("Student Details")
        print("Name:", self.__name)
        print("Roll Number:", self.__roll_number)
        print("Marks:", self.__marks)


S = Student("Rahul", 101, 85)
S.display_details()

print("\nAfter updating marks using encapsulation")
S.set_marks(90)
print("Updated Marks:", S.get_marks())
