try:
    student_marks = {
        "Alice": 85,
        "Bob": 90,
        "Charlie": 78
    }

    student_name = input("Enter student name: ")
    print(student_name, "scored", student_marks[student_name], "marks.")

except KeyError:
    print("Error: Student name not found in the records.")

finally:
    print("Key error handling program completed.")
