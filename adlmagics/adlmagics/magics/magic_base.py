from pandas import DataFrame

from adlmagics.session_consts import session_null_value
from adlmagics.exceptions import MagicArgumentError

class MagicBase:
    def __init__(self, cmd_name, session_service, presenter_factory):
        self.cmd_name = cmd_name
        self._session_service = session_service
        self.__presenter_factory = presenter_factory

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
        self.__presenter_factory.present(obj)