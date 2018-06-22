class PresenterBase:
    def __init__(self, target_type):
        self.__target_type = target_type

    def present(self, obj):
        pass

    @property
    def target_type(self):
        return self.__target_type