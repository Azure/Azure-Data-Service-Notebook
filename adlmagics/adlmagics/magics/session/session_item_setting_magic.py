from IPython.core.magic_arguments import magic_arguments, argument, parse_argstring

from adlmagics.magics.session.session_magic_base import SessionMagicBase
from adlmagics.exceptions import MagicArgumentMissingError, MagicArgumentError

class SessionItemSettingMagic(SessionMagicBase):
    def __init__(self, session_service, presenter_factory):
        super(SessionItemSettingMagic, self).__init__("setsessionitem", session_service, presenter_factory)
    
    @magic_arguments()
    @argument("--name", type = str, help = "Session item name.")
    @argument("--value", type = str, help = "Session item new value.")
    def execute(self, arg_string, content_string = None):
        args = parse_argstring(self.execute, arg_string)

        self.__validate_args(args)

        self._session_service.set_session_item(args.name, args.value)

        self._present("%s set to %s" % (args.name, self._session_service.get_session_item(args.name)))

    def __validate_args(self, args):
        if not args.name:
            raise MagicArgumentMissingError("name")

        if not self._session_service.contains_session_item(args.name):
            raise MagicArgumentError("Session item '%s' not supported." % (args.name))