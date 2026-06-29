from pathlib import Path


class FileWriter:
    def __init__(self, file_name):
        self.file_name = Path(__file__).parent / file_name

    def write_message(self, message):
        with open(self.file_name, "w") as file:
            file.write(message)

    def read_message(self):
        with open(self.file_name, "r") as file:
            return file.read()


writer = FileWriter("class_object_demo.txt")
writer.write_message("This file was created using a class and object.")

print("File Content:")
print(writer.read_message())
