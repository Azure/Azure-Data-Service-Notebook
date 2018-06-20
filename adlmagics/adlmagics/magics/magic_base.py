from IPython.core.display import display, HTML
from sys import stdout
from os import linesep
from pandas import DataFrame
from pandas.core.config import option_context

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
        if (not models):
            return DataFrame()

        if (len(models) == 0):
            return DataFrame()
        
        property_names = [property_name for property_name in models[0].__dict__ if not property_name.startswith("_")]
        
        #hack: should have a better method instead
        with option_context('display.max_rows', None):
            data = DataFrame([[getattr(model, property_name) for property_name in property_names] for model in models], columns = property_names)
        return data