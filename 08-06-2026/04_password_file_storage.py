from pathlib import Path


class PasswordFileError(Exception):
    pass


class PasswordStorage:
    def __init__(self, file_name):
        self.file_path = Path(__file__).parent / file_name

    def save_password(self, username, password):
        try:
            if not username or not password:
                raise PasswordFileError("Username and password cannot be empty.")

            with open(self.file_path, "a") as file:
                file.write(f"{username}: {password}\n")

            print("Password saved to file.")
        except PasswordFileError as error:
            print("Storage Error:", error)
        except PermissionError:
            print("Storage Error: Permission denied.")

    def show_passwords(self):
        try:
            with open(self.file_path, "r") as file:
                print(file.read())
        except FileNotFoundError:
            print("Storage Error: Password file was not found.")


storage = PasswordStorage("password_records.txt")
storage.save_password("student", "CodeBind@123")
storage.save_password("", "")

print("Stored Passwords:")
storage.show_passwords()
