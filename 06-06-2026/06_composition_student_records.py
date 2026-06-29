from pathlib import Path


class FileStorage:
    def __init__(self, file_name):
        self.file_name = Path(__file__).parent / file_name

    def save(self, data):
        with open(self.file_name, "a") as file:
            file.write(data + "\n")

    def read_all(self):
        with open(self.file_name, "r") as file:
            return file.readlines()


class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def to_record(self):
        return f"{self.roll_no}, {self.name}, {self.marks}"


class StudentRecordManager:
    def __init__(self, storage):
        self.storage = storage

    def add_student(self, student):
        self.storage.save(student.to_record())

    def show_students(self):
        for record in self.storage.read_all():
            print(record.strip())


storage = FileStorage("student_records.txt")
manager = StudentRecordManager(storage)

manager.add_student(Student(101, "Asha", 88))
manager.add_student(Student(102, "Ravi", 92))

print("Student Records:")
manager.show_students()
