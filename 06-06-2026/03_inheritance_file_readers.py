from pathlib import Path


class FileReader:
    def __init__(self, file_name):
        self.file_name = Path(__file__).parent / file_name

    def read_file(self):
        with open(self.file_name, "r") as file:
            return file.read()


class TextFileReader(FileReader):
    def display_text(self):
        print("Text File Content:")
        print(self.read_file())


with open(Path(__file__).parent / "inheritance_demo.txt", "w") as file:
    file.write("Inheritance allows TextFileReader to reuse FileReader methods.")

reader = TextFileReader("inheritance_demo.txt")
reader.display_text()
