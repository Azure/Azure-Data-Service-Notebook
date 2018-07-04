from pandas import DataFrame

from adlmagics.magics.magic_base import MagicBase

class MagicWithResultBase(MagicBase):
    def __init__(self, cmd_name, session_service, presenter_factory, result_converter):
        super(MagicWithResultBase, self).__init__(cmd_name, session_service, presenter_factory)

        self._result_converter = result_converter

    def _convert_result(self, result):
        converted_result = self._result_converter.convert(result)

        if isinstance(converted_result, DataFrame):
            self._present("The result is pandas' DataFrame, you can call functions accordingly.")
        
        return converted_result

    