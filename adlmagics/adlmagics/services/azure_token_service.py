from sys import stdout
from os import linesep
from adal import AuthenticationContext
from threading import Timer
from msrestazure.azure_active_directory import AADTokenCredentials

class AzureTokenService:
    client_id = "04b07795-8ddb-461a-bbee-02f9e1bf7b46"
    authority_url_format = "https://login.microsoftonline.com/{0}"
    resource_url = "https://management.core.windows.net/"

    token_refresh_offset_in_seconds = -60

    def __init__(self):
        self.__tenant = None
        self.__tenant_id = None
        self.__logged_in_user = None
        self.__token = None
        self.__credentials = None
        self.__refresh_token_timer = None

    def login(self, tenant):
        auth_context = AuthenticationContext(AzureTokenService.authority_url_format.format(tenant))
        user_code = auth_context.acquire_user_code(AzureTokenService.resource_url, AzureTokenService.client_id)
        self.__write_line(user_code['message'])

        self.__token = auth_context.acquire_token_with_device_code(AzureTokenService.resource_url, user_code, AzureTokenService.client_id)

        self.__tenant = tenant
        self.__tenant_id = self.__token["tenantId"]
        self.__logged_in_user = self.__token["userId"]
        self.__credentials = AADTokenCredentials(self.__token, AzureTokenService.client_id)
        
        self.__update_refresh_token_timer()

    def logout(self):
        self.__tenant = None
        self.__tenant_id = None
        self.__logged_in_user = None
        self.__token = None
        self.__credentials = None
        if (self.__refresh_token_timer):
            self.__refresh_token_timer.cancel()
            self.__refresh_token_timer = None

    @property
    def tenant(self):
        return self.__tenant

    @property
    def tenant_id(self):
        return self.__tenant_id

    @property
    def logged_in_user(self):
        return self.__logged_in_user

    @property
    def token(self):
        return self.__token

    @property
    def credentials(self):
        return self.__credentials

    def __do_refresh_token(self):
        auth_context = AuthenticationContext(AzureTokenService.authority_url_format.format(self.__tenant_id))
        self.__token = auth_context.acquire_token_with_refresh_token(self.__token["refreshToken"], AzureTokenService.client_id, AzureTokenService.resource_url)
        self.__credentials = AADTokenCredentials(self.__token, AzureTokenService.client_id)

        self.__update_refresh_token_timer()

    def __update_refresh_token_timer(self):
        if (self.__refresh_token_timer):
            self.__refresh_token_timer.cancel()
        refresh_token_timer_interval = self.__token["expiresIn"] + AzureTokenService.token_refresh_offset_in_seconds
        self.__refresh_token_timer = Timer(refresh_token_timer_interval, self.__do_refresh_token)
        self.__refresh_token_timer.start()
    
    def __write_line(self, text):
        stdout.write(text + linesep)