from azure.mgmt.resource.subscriptions import SubscriptionClient
from azure.mgmt.datalake.store import DataLakeStoreAccountManagementClient
from azure.mgmt.datalake.store.models import DataLakeStoreAccount
from azure.datalake.store import core, lib
from uuid import uuid4
from time import time
from datetime import datetime
from sys import stdout
from platform import platform

from adlmagics.exceptions import UserNotLoggedInError
from adlmagics.models.adls_account import AdlsAccount
from adlmagics.models.adls_folder import AdlsFolder
from adlmagics.models.adls_file import AdlsFile

CONST_WINDOW_STR = "windows"
CONST_WINDOW_UTF_8_ENCODE = "utf-8-sig"

class AdlsServiceSdkImpl:
    def __init__(self, token_service):
        self.__token_service = token_service

    def retrieve_accounts(self, page_index, page_account_number):
        if (not self.__token_service.logged_in_user):
            raise UserNotLoggedInError()

        accounts = []

        sub_client = SubscriptionClient(self.__token_service.credentials)
        for sub in sub_client.subscriptions.list():
            dls_client = DataLakeStoreAccountManagementClient(self.__token_service.credentials, sub.subscription_id)
            accounts.extend([AdlsAccount(account.name) for account in dls_client.accounts.list()])

        accounts.sort(key = lambda account: getattr(account, "name"))
            
        skipped_account_number = page_index * page_account_number
        return accounts[skipped_account_number : skipped_account_number + page_account_number]

    def retrieve_files(self, account, folder_path):
        if (not self.__token_service.logged_in_user):
            raise UserNotLoggedInError()

        adls_fs_client = self.__create_fs_client(account)

        # schema sample: {'length': 3019, 'pathSuffix': 'ASAUnmappedEventCounts.tsv', 'type': 'FILE', 'blockSize': 268435456, 'accessTime': 1520868025889, 'modificationTime': 1520868025953, 'replication': 1, 'permission': '770', 'owner': '07fa3c98-617e-46be-9648-217d8dd51f0d', 'group': 'e292a513-1aca-454b-9975-fbadafc7ebc8', 'msExpirationTime': 0, 'aclBit': True, 'name': 'vifeng/ASAUnmappedEventCounts.tsv'}
        return [AdlsFile(f["pathSuffix"], f["name"], int(f["length"]), datetime.fromtimestamp(int(f["accessTime"]) / 1000), datetime.fromtimestamp(int(f["modificationTime"]) / 1000)) for f in adls_fs_client.ls(folder_path, detail = True) if f["type"] == "FILE"]

    def retrieve_folders(self, account, folder_path):
        if (not self.__token_service.logged_in_user):
            raise UserNotLoggedInError()

        adls_fs_client = self.__create_fs_client(account)
        
        # schema sample: {'length': 0, 'pathSuffix': 'MonthlyUserIds', 'type': 'DIRECTORY', 'blockSize': 0, 'accessTime': 1499323953990, 'modificationTime': 1499331875161, 'replication': 0, 'permission': '770', 'owner': 'e292a513-1aca-454b-9975-fbadafc7ebc8', 'group': 'e292a513-1aca-454b-9975-fbadafc7ebc8', 'aclBit': True, 'name': 'vifeng/MonthlyUserIds'}
        return [AdlsFolder(f["pathSuffix"], f["name"], datetime.fromtimestamp(int(f["accessTime"]) / 1000), datetime.fromtimestamp(int(f["modificationTime"]) / 1000)) for f in adls_fs_client.ls(folder_path, detail = True) if f["type"] == "DIRECTORY"]

    def read_file(self, account, file_path, encoding, column_sep, to_be_read_line_count):
        if (not self.__token_service.logged_in_user):
            raise UserNotLoggedInError()

        adls_fs_client = self.__create_fs_client(account)

        read_lines = []
        read_line_count = 0
        with adls_fs_client.open(file_path) as f:
            for read_line in f:
                # if platform is `window` and `encoding` is `utf-8`, change it to `utf-8-sig` for avoiding werid `\ufeff` problems
                if(CONST_WINDOW_STR in platform().lower() and encoding.lower().strip() == "utf-8"):
                    encoding = CONST_WINDOW_UTF_8_ENCODE
                read_lines.append(read_line.decode(encoding).strip().split(column_sep))
                read_line_count += 1
                if (read_line_count >= to_be_read_line_count):
                    break

        return read_lines

    def __create_fs_client(self, account):
        token = self.__token_service.token
        # Copied from azure.datalake.store.lib, since AzureDLFileSystem requires a different form of token than that provided by our token service.
        token.update({
            'access': token['accessToken'],
            'resource': lib.DEFAULT_RESOURCE_ENDPOINT,
            'refresh': token.get('refreshToken', False),
            'time': time(),
            'tenant': self.__token_service.tenant_id,
            'client': lib.default_client})

        return core.AzureDLFileSystem(token = lib.DataLakeCredential(token), store_name = account)