from IPython.core.magic_arguments import magic_arguments, argument, parse_argstring

from adlmagics.magics.session.session_magic_base import SessionMagicBase
from adlmagics.exceptions import MagicArgumentMissingError, MagicArgumentError

class SessionItemSettingMagic(SessionMagicBase):
    def __init__(self, cmd_name, session_service, presenter_factory):
        super(SessionListingMagic, self).__init__("setsessionitem", session_service, presenter_factory)
    
    @magic_arguments()
    @argument("--name", type = str, help = "Session item name.")
    @argument("--value", type = str, help = "Session item new value.")
    def execute(self, arg_string, content_string):
        args = parse_argstring(execute, arg_string)

        self.__validate_args(args)

        for session_item_name in self._session_service.session_item_names:
            self._present("%s : %s" % (session_item_name, self._session_service.get_session_item(session_item_name)))

    def __validate_args(self, args):
        if not args.name:
            raise MagicArgumentMissingError("name")

        if not self._session_service.contains_session_item(name):
            raise MagicArgumentError("Session item '%s' not supported." % (name))