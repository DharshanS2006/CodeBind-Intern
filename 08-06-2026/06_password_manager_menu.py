class PasswordNotFoundError(Exception):
    pass


class PasswordManager:
    def __init__(self):
        self.__passwords = {}

    def add_password(self, account_name, password):
        try:
            if account_name in self.__passwords:
                raise KeyError("Account already exists.")
            if len(password) < 8:
                raise ValueError("Password must contain at least 8 characters.")

            self.__passwords[account_name] = password
            print("Password added successfully.")
        except KeyError as error:
            print("Manager Error:", error)
        except ValueError as error:
            print("Manager Error:", error)

    def get_password(self, account_name):
        try:
            if account_name not in self.__passwords:
                raise PasswordNotFoundError("Password not found for this account.")

            print("Password:", self.__passwords[account_name])
        except PasswordNotFoundError as error:
            print("Manager Error:", error)


manager = PasswordManager()
manager.add_password("gmail", "Gmail@123")
manager.add_password("gmail", "Another@123")
manager.add_password("github", "git")

manager.get_password("gmail")
manager.get_password("facebook")
