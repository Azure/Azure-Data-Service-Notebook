from pandas import DataFrame
from pandas.core.config import set_option

class MatrixToDataFrameConverter:
    def __init__(self):
        set_option('display.max_rows', None)

    def convert(self, obj):
        if (not obj) or (not obj is list) or (len(obj) == 0):
            return DataFrame()

        return DataFrame(obj)