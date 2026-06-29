from pathlib import Path


class SafeFileReader:
    def __init__(self, file_name):
        self.file_name = Path(__file__).parent / file_name

    def read_file(self):
        try:
            with open(self.file_name, "r") as file:
                return file.read()
        except FileNotFoundError:
            return "Error: File not found."
        except PermissionError:
            return "Error: Permission denied."


reader = SafeFileReader("missing_file.txt")
print(reader.read_file())
