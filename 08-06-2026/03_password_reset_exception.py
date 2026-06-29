class SamePasswordError(Exception):
    pass


class PasswordReset:
    def __init__(self, current_password):
        self.__current_password = current_password

    def reset_password(self, old_password, new_password):
        try:
            if old_password != self.__current_password:
                raise ValueError("Old password is incorrect.")
            if new_password == self.__current_password:
                raise SamePasswordError("New password cannot be same as old password.")
            if len(new_password) < 8:
                raise ValueError("New password must contain at least 8 characters.")

            self.__current_password = new_password
            print("Password reset successfully.")
        except ValueError as error:
            print("Password Reset Error:", error)
        except SamePasswordError as error:
            print("Password Reset Error:", error)


reset = PasswordReset("CodeBind@123")
reset.reset_password("wrongpass", "NewPass@123")
reset.reset_password("CodeBind@123", "CodeBind@123")
reset.reset_password("CodeBind@123", "NewPass@123")
