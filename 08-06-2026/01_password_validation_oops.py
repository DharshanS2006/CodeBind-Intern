class WeakPasswordError(Exception):
    pass


class PasswordValidator:
    def __init__(self, password):
        self.password = password

    def validate(self):
        try:
            if len(self.password) < 8:
                raise WeakPasswordError("Password must contain at least 8 characters.")
            if not any(char.isdigit() for char in self.password):
                raise WeakPasswordError("Password must contain at least one number.")
            if not any(char.isupper() for char in self.password):
                raise WeakPasswordError("Password must contain at least one uppercase letter.")

            print("Password is strong.")
        except WeakPasswordError as error:
            print("Validation Error:", error)


validator = PasswordValidator("Code123")
validator.validate()

validator = PasswordValidator("CodeBind123")
validator.validate()
