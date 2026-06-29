class Student:
    def __init__(self):
        self.name = "Anita"
        self.roll_number = 102
        self.course = "Python"

    def display_details(self):
        print("Student Details")
        print("Name:", self.name)
        print("Roll Number:", self.roll_number)
        print("Course:", self.course)


S = Student()
S.display_details()
    