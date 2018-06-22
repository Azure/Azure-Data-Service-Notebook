from sys import stdout
from os import linesep

from adlmagics.interfaces.presenter_base import PresenterBase

class TextPresenter(PresenterBase):
    def __init__(self):
        super(TextPresenter, self).__init__(str)

    def present(self, obj):
        if (not obj) or (not obj is str):
            stdout.write(linesep)
        else:
            stdout.write(text + linesep)