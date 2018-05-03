from magics.azure.azure_magic_base import AzureMagicBase

class AzureLogoutMagic(AzureMagicBase):
    def __init__(self, token_service):
        super(AzureLogoutMagic, self).__init__("logout", token_service)

    def execute(self, arg_string, content_string = None):
        tenant = self._token_service.tenant
        user = self._token_service.logged_in_user
        
        self._token_service.logout()

        self._write_line("User '%s' logged out of tenant '%s'" % (user, tenant))
        
        
        