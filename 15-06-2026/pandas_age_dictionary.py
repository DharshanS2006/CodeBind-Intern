import pandas as pd

n = int(input("Enter the number of students: "))

students = {}

for i in range(n):
    name = input(f"Enter name of student {i+1}: ")
    age = int(input(f"Enter age of {name}: "))
    students[name] = age

student_age_series = pd.Series(students)

print("\nStudent Age Series:")
print(student_age_series)