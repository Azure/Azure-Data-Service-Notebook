from pandas import DataFrame
from pandas.core.config import set_option

class ObjectToDataFrameConverter:
    def __init__(self):
        set_option('display.max_rows', None)

    def convert(self, obj):
        if not obj:
            return DataFrame()

        if (obj is list) and (len(obj) > 0):
            property_names = [property_name for property_name in obj[0].__dict__ if not property_name.startswith("_")]
            return DataFrame([[getattr(o, property_name) for property_name in property_names] for o in obj], columns = property_names)
        else:
            property_names = [property_name for property_name in obj.__dict__ if not property_name.startswith("_")]
            return DataFrame([getattr(obj, property_name) for property_name in property_names], columns = property_names)