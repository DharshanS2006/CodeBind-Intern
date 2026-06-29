class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def display_details(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_number)
        print("Marks:", self.marks)

students = []
n = int(input("Enter number of students: "))

for i in range(n):
    print("\nEnter details for student", i + 1)
    name = input("Enter student name: ")
    roll_number = input("Enter roll number: ")
    marks = input("Enter marks: ")

    S = Student(name, roll_number, marks)
    students.append(S)

print("\nAll Student Details")
for S in students:
    S.display_details()
    print()
