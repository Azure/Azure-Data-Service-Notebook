class UserNotLoggedInError(Exception):
    def __init__(self):
        super(UserNotLoggedInError, self).__init__("User not logged in.")
