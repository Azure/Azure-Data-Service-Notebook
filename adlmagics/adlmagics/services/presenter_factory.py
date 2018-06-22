from adlmagics.presenters.presenter_base import PresenterBase

class PresenterFactory:
    def __init__(self):
        self.__presenters = dict()

    def register_presenter(self, target_type, presenter):
        if (not target_type) or (not presenter) or (not presenter is PresenterBase):
            return

        self.__presenters.setdefault(target_type, []).append(presenter)

    def get_presenters(self, target_type):
        if (not target_type):
            return []

        return self.__presenters.setdefault(target_type, [])