class UserNotLoggedInError(Exception):
    def __init__(self):
        super(UserNotLoggedInError, self).__init__("User not logged in.")

class MagicArgumentMissingError(Exception):
    def __init__(self, arg_name):
        super(MagicArgumentMissingError, self).__init__("Argument '%s' is missing" % (arg_name))

class MagicArgumentError(Exception):
    def __init__(self, msg):
        super(MagicArgumentError, self).__init__(msg)