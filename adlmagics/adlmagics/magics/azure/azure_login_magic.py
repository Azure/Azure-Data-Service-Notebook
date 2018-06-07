from IPython.core.magic_arguments import magic_arguments, argument, parse_argstring

from adlmagics.magics.azure.azure_magic_base import AzureMagicBase

class AzureLoginMagic(AzureMagicBase):
    def __init__(self, token_service):
        super(AzureLoginMagic, self).__init__("login", token_service)

    @magic_arguments()
    @argument("--tenant", type = str, help = "Azure tenant name or id.")
    def execute(self, arg_string, content_string = None):
        args = parse_argstring(self.execute, arg_string)

        self._write_line("Waiting for user login...")

        self._token_service.login(args.tenant)

        self._write_line("User '%s' logged in to tenant '%s'" % (self._token_service.logged_in_user, self._token_service.tenant))