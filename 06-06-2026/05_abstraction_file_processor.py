from abc import ABC, abstractmethod
from pathlib import Path


class FileProcessor(ABC):
    def __init__(self, file_name):
        self.file_name = Path(__file__).parent / file_name

    @abstractmethod
    def process(self):
        pass


class WordCounter(FileProcessor):
    def process(self):
        with open(self.file_name, "r") as file:
            text = file.read()
            words = text.split()
            return len(words)


with open(Path(__file__).parent / "abstraction_demo.txt", "w") as file:
    file.write("Abstraction shows only important details to the user.")

counter = WordCounter("abstraction_demo.txt")
print("Total Words:", counter.process())
