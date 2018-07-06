from IPython import get_ipython

class IPShellResultReceiver:
    def __init__(self):
        self.__shell = get_ipython()

    def receive(self, result_name, result_value):
        self.__shell.user_ns[result_name] = result_value