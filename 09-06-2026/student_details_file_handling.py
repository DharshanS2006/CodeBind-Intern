from pathlib import Path


class InvalidStudentDataError(Exception):
    pass


class Student:
    def __init__(self, roll_no, name, age, course):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.course = course

    def validate(self):
        if self.roll_no <= 0:
            raise InvalidStudentDataError("Roll number must be greater than zero.")
        if not self.name.strip():
            raise InvalidStudentDataError("Student name cannot be empty.")
        if self.age <= 0:
            raise InvalidStudentDataError("Age must be greater than zero.")
        if not self.course.strip():
            raise InvalidStudentDataError("Course cannot be empty.")

    def to_file_record(self):
        return f"Roll No: {self.roll_no}, Name: {self.name}, Age: {self.age}, Course: {self.course}"


class StudentFileManager:
    def __init__(self, file_name):
        self.file_path = Path(__file__).parent / file_name

    def save_student(self, student):
        try:
            student.validate()

            with open(self.file_path, "a") as file:
                file.write(student.to_file_record() + "\n")

            print("Student details saved successfully.")
            return True
        except InvalidStudentDataError as error:
            print("Student Data Error:", error)
        except PermissionError:
            print("File Error: Permission denied while writing student details.")
        except OSError as error:
            print("File Error:", error)
        return False

    def show_all_students(self):
        try:
            with open(self.file_path, "r") as file:
                records = file.read()

            if records:
                print("\nSaved Student Details:")
                print(records)
            else:
                print("No student details found.")
        except FileNotFoundError:
            print("File Error: Students_details.txt file was not found.")
        except OSError as error:
            print("File Error:", error)


class ErrorReminder:
    def show_name_error(self):
        try:
            raise NameError("A variable is used before it is defined.")
        except NameError as error:
            print("NameError:", error)

    def show_type_error(self):
        try:
            raise TypeError("An operation is done using the wrong data type.")
        except TypeError as error:
            print("TypeError:", error)

    def show_value_error(self):
        try:
            number = int("abc")
            print(number)
        except ValueError as error:
            print("ValueError:", error)

    def show_index_error(self):
        try:
            raise IndexError("A list position is used that does not exist.")
        except IndexError as error:
            print("IndexError:", error)

    def show_file_not_found_error(self):
        try:
            with open(Path(__file__).parent / "missing_students_file.txt", "r") as file:
                print(file.read())
        except FileNotFoundError as error:
            print("FileNotFoundError:", error)

    def show_zero_division_error(self):
        try:
            raise ZeroDivisionError("A number cannot be divided by zero.")
        except ZeroDivisionError as error:
            print("ZeroDivisionError:", error)

    def show_key_error(self):
        try:
            raise KeyError("A dictionary key is used that does not exist.")
        except KeyError as error:
            print("KeyError:", error)

    def show_attribute_error(self):
        try:
            raise AttributeError("An object is used with an attribute it does not have.")
        except AttributeError as error:
            print("AttributeError:", error)

    def show_all_errors(self):
        print("Common Python Error Reminders:")
        self.show_name_error()
        self.show_type_error()
        self.show_value_error()
        self.show_index_error()
        self.show_file_not_found_error()
        self.show_zero_division_error()
        self.show_key_error()
        self.show_attribute_error()
        print()


class StudentApp:
    def __init__(self):
        self.manager = StudentFileManager("Students_details.txt")
        self.error_reminder = ErrorReminder()

    def get_positive_integer(self, message):
        while True:
            try:
                value = int(input(message))
                if value <= 0:
                    raise ValueError("Value must be greater than zero.")
                return value
            except ValueError as error:
                print("Input Error:", error)

    def get_non_empty_text(self, message):
        while True:
            try:
                value = input(message).strip()
                if not value:
                    raise ValueError("This field cannot be empty.")
                return value
            except ValueError as error:
                print("Input Error:", error)

    def ask_to_show_error_reminders(self):
        choice = input("Do you want to see common error reminders? (yes/no): ").strip().lower()
        if choice == "yes":
            self.error_reminder.show_all_errors()

    def run(self):
        self.ask_to_show_error_reminders()
        total_students = self.get_positive_integer("Enter number of students: ")

        for index in range(total_students):
            print(f"\nEnter details for student {index + 1}")

            roll_no = self.get_positive_integer("Enter roll number: ")
            name = self.get_non_empty_text("Enter name: ")
            age = self.get_positive_integer("Enter age: ")
            course = self.get_non_empty_text("Enter course: ")

            student = Student(roll_no, name, age, course)
            self.manager.save_student(student)

        self.manager.show_all_students()


if __name__ == "__main__":
    app = StudentApp()
    app.run()
