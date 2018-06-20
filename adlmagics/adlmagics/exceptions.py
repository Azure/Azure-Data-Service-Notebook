class UserNotLoggedInError(Exception):
    def __init__(self):
        super(UserNotLoggedInError, self).__init__("User not logged in.")

class ValidationError(Exception):
    def __init__(self, val):
        super(ValidationError, self).__init__(val)