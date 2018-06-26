from sys import stdout
from os import linesep

from adlmagics.presenters.presenter_base import PresenterBase

class TextPresenter(PresenterBase):
    def is_presentable(self, obj):
        return isinstance(obj, str)

    def present(self, obj):
        super(TextPresenter, self).present(obj)

        stdout.write(text + linesep)