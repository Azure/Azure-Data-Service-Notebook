from pandas import DataFrame

from adlmagics.session_consts import session_null_value
from adlmagics.exceptions import MagicArgumentError

class MagicBase:
    def __init__(self, cmd_name, session_service, presenter_factory, result_converter):
        self.cmd_name = cmd_name
        self._session_service = session_service
        self._presenter_factory = presenter_factory
        self._result_converter = result_converter

    def execute(self, arg_string, content_string):
        pass

    def _validate_arg(self, args, arg_name, session_item_name):
        if (not getattr(args, arg_name)):
            sessioned_value = self._session_service.get_session_item(session_item_name)
            if (session_null_value == sessioned_value):
                raise MagicArgumentError("Please specify argument '%s' or use setsession magic to set a value for session item '%s'" % (arg_name, session_item_name))
            else:
                setattr(args, arg_name, sessioned_value)

    def _present(self, obj):
        presenters = self._presenter_factory.get_presenters(type(obj))
        if (not presenters) or len(presenters) == 0:
            return

        for presenter in presenters:
            presenter.present(obj)

    def _convert_result(self, result):
        converted = self._result_converter.convert(result)

        if converted is DataFrame:
            self._present("The result is pandas' DataFrame, you can call functions accordingly.")
        
        return converted