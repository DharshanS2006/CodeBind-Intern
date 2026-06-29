from pathlib import Path


class FileManager:
    def __init__(self, file_name):
        self.__file_name = Path(__file__).parent / file_name

    def add_line(self, line):
        with open(self.__file_name, "a") as file:
            file.write(line + "\n")

    def show_lines(self):
        with open(self.__file_name, "r") as file:
            for line in file:
                print(line.strip())

    def get_file_name(self):
        return self.__file_name


manager = FileManager("encapsulation_demo.txt")
manager.add_line("Encapsulation keeps file details inside the class.")
manager.add_line("The file name is private and accessed through methods.")

print("File Name:", manager.get_file_name())
print("File Content:")
manager.show_lines()
