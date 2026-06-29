class InvalidPasswordError(Exception):
    pass


class UserAccount:
    def __init__(self, username, password):
        self.username = username
        self.__password = password
        self.login_attempts = 0

    def login(self, entered_password):
        try:
            if entered_password != self.__password:
                self.login_attempts += 1
                raise InvalidPasswordError("Incorrect password entered.")

            print("Login successful. Welcome", self.username)
        except InvalidPasswordError as error:
            print("Login Error:", error)
            print("Attempts:", self.login_attempts)


account = UserAccount("student", "Python@123")
account.login("python123")
account.login("Python@123")
