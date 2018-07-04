from IPython.core.interactiveshell import InteractiveShellABC

class IPShellResultReceiver:
    def __init__(self):
        self.__shell = InteractiveShellABC()

    def receive(self, result_name, result_value):
        self.__shell.user_ns[result_name] = result_value