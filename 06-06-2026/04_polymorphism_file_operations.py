from pathlib import Path


class TextFile:
    def save(self, file_name, content):
        with open(Path(__file__).parent / file_name, "w") as file:
            file.write(content)


class LogFile:
    def save(self, file_name, content):
        with open(Path(__file__).parent / file_name, "a") as file:
            file.write("[LOG] " + content + "\n")


def store_file(file_object, file_name, content):
    file_object.save(file_name, content)


text_file = TextFile()
log_file = LogFile()

store_file(text_file, "polymorphism_text.txt", "Saved by TextFile class.")
store_file(log_file, "polymorphism_log.txt", "Saved by LogFile class.")
store_file(log_file, "polymorphism_log.txt", "Another log entry.")

print("Files saved using polymorphism.")
