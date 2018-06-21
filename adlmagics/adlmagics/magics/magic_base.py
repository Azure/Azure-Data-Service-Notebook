from IPython.core.display import display, HTML
from sys import stdout
from os import linesep
from pandas import DataFrame
from pandas.core.config import set_option

class MagicBase:
    def __init__(self, cmd_name):
        self.cmd_name = cmd_name

    def _write_line(self, text = None):
        if (text):
            stdout.write(text + linesep)
        else:
            stdout.write(linesep)

    def _write_html(self, html_string):
        display(HTML(html_string))

    def _convert_to_df(self, models):
        if (not models or len(models) == 0):
            return []

        property_names = [property_name for property_name in models[0].__dict__ if not property_name.startswith("_")]
        
        
        set_option('display.max_rows', None)
        return DataFrame([[getattr(model, property_name) for property_name in property_names] for model in models], columns = property_names)
        