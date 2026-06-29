class Student:
    def __init__(self, name, roll_number, marks):
        self.__name = name
        self.__roll_number = roll_number
        self.__marks = marks

    def get_name(self):
        return self.__name

    def get_roll_number(self):
        return self.__roll_number

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        self.__marks = marks


class StudentDetails(Student):
    def __init__(self, name, roll_number, marks, course):
        super().__init__(name, roll_number, marks)
        self.__course = course

    def get_course(self):
        return self.__course

    def display_details(self):
        print("Name:", self.get_name())
        print("Roll Number:", self.get_roll_number())
        print("Marks:", self.get_marks())
        print("Course:", self.__course)


students = []
n = int(input("Enter number of students: "))

for i in range(n):
    print("\nEnter details for student", i + 1)
    name = input("Enter student name: ")
    roll_number = input("Enter roll number: ")
    marks = input("Enter marks: ")
    course = input("Enter course: ")

    S = StudentDetails(name, roll_number, marks, course)
    students.append(S)

print("\nAll Student Details")
for S in students:
    S.display_details()
    print()
