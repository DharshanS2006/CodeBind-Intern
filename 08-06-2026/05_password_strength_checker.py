class PasswordStrengthChecker:
    def __init__(self, password):
        self.password = password

    def check_strength(self):
        try:
            score = 0

            if len(self.password) >= 8:
                score += 1
            if any(char.isupper() for char in self.password):
                score += 1
            if any(char.islower() for char in self.password):
                score += 1
            if any(char.isdigit() for char in self.password):
                score += 1
            if any(not char.isalnum() for char in self.password):
                score += 1

            if score <= 2:
                raise ValueError("Weak password.")
            if score <= 4:
                print("Medium password.")
            else:
                print("Strong password.")
        except TypeError:
            print("Error: Password must be text.")
        except ValueError as error:
            print("Strength Error:", error)


checker = PasswordStrengthChecker("pass")
checker.check_strength()

checker = PasswordStrengthChecker("CodeBind@123")
checker.check_strength()
