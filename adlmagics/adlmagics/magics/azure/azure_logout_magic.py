from adlmagics.magics.azure.azure_magic_base import AzureMagicBase

from adlmagics.session_consts import session_tenant, session_user, session_null_value

class AzureLogoutMagic(AzureMagicBase):
    def __init__(self, session_service, presenter_factory, token_service):
        super(AzureLogoutMagic, self).__init__("logout", session_service, presenter_factory, token_service)

    def execute(self, arg_string, content_string = None):
        tenant = self._token_service.tenant
        user = self._token_service.logged_in_user
        
        self._token_service.logout()

        self._session_service.set_session_item(session_tenant.name, session_null_value)
        self._session_service.set_session_item(session_user.name, session_null_value)

        self._present("User '%s' logged out of tenant '%s'" % (user, tenant))