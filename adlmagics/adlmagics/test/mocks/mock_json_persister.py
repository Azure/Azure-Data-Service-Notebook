from json import loads, dumps

class MockJsonPersister:
    def __init__(self):
        self.__json = "{}"

    def load(self):
        return loads(self.__json)

    def save(self, obj):
        self.__json = dumps(obj, ensure_ascii = False)