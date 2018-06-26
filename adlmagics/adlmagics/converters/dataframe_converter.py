from pandas import DataFrame
from pandas.core.config import set_option

class DataFrameConverter:
    def __init__(self):
        set_option('display.max_rows', None)

    def convert(self, obj):
        if not obj:
            return DataFrame()

        if isinstance(obj, list):
            # obj is a list
            if len(obj) > 0:
                first_obj = obj[0]
                if hasattr(first_obj, "__dict__"):
                    # obj is a list of models
                    property_names = [property_name for property_name in first_obj.__dict__ if not property_name.startswith("_")]
                    if len(property_names) > 0:
                        return DataFrame([[getattr(o, property_name) for property_name in property_names] for o in obj], columns = property_names)
                elif isinstance(first_obj, list):
                    # obj is a matrix
                    return DataFrame(obj)
            else:
                # The list is empty
                return DataFrame()
        else:
            if hasattr(obj, "__dict__"):
                # obj is a model
                property_names = [property_name for property_name in obj.__dict__ if not property_name.startswith("_")]
                if len(property_names) > 0:
                    return DataFrame([[getattr(obj, property_name) for property_name in property_names]], columns = property_names)

        raise ValueError("Not convertible to DataFrame.")