from IPython.core.magic_arguments import magic_arguments, argument, parse_argstring

from adlmagics.magics.azure.azure_magic_base import AzureMagicBase
from adlmagics.session_consts import session_tenant, session_user
from adlmagics.exceptions import MagicArgumentMissingError

class AzureLoginMagic(AzureMagicBase):
    def __init__(self, session_service, presenter_factory, token_service):
        super(AzureLoginMagic, self).__init__("login", session_service, presenter_factory, token_service)

    @magic_arguments()
    @argument("--tenant", type = str, help = "Azure tenant name or id.")
    def execute(self, arg_string, content_string = None):
        args = parse_argstring(self.execute, arg_string)

        self.__validate_args(args)

        self._present("Waiting for user login...")

        self._token_service.login(args.tenant)

        self._session_service.set_session_item(session_tenant.name, self._token_service.tenant)
        self._session_service.set_session_item(session_user.name, self._token_service.logged_in_user)

        self._present("User '%s' logged in to tenant '%s'" % (self._token_service.logged_in_user, self._token_service.tenant))

    def __validate_args(self, args):
        if not args.tenant:
            raise MagicArgumentMissingError("tenant")