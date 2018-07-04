from adlmagics.presenters.presenter_base import PresenterBase

class PresenterFactory:
    def __init__(self):
        self.__presenters = []

    def register_presenter(self, presenter):
        if not isinstance(presenter, PresenterBase):
            return

        self.__presenters.append(presenter)

    def present(self, obj):
        if (not obj):
            return

        for presenter in self.__presenters:
            if presenter.is_presentable(obj):
                presenter.present(obj)