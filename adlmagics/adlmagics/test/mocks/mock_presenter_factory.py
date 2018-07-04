class MockPresenterFactory:
    def __init__(self):
        self.__presented_logs = []

    def register_presenter(self, presenter):
        pass

    def present(self, obj):
        text = ""
        if isinstance(obj, str):
            text = obj
        elif isinstance(obj, list):
            if len(obj) > 0:
                text = "A list of %s" % (type(obj[0]).__name__)
            else:
                text = "A list"
        else:
            text = type(obj).__name__

        self.__presented_logs.append(text)

    def clear(self):
        self.__presented_logs.clear()

    @property
    def presented_logs(self):
        return self.__presented_logs