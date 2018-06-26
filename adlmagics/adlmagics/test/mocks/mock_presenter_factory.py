class MockPresenterFactory:
    def __init__(self):
        self.__presented_logs = []

    def register_presenter(self, presenter):
        pass

    def present(self, obj):
        text = ""
        if not isinstance(obj, str):
            text = type(obj).__name__
        else:
            text = obj

        self.__presented_logs.append(text)

    @property
    def presented_logs(self):
        return self.__presented_logs