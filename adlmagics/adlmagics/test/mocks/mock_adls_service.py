from datetime import datetime
from uuid import uuid4

from adlmagics.models.adls_account import AdlsAccount
from adlmagics.models.adls_folder import AdlsFolder
from adlmagics.models.adls_file import AdlsFile

class MockAdlsService:
    def __init__(self, token_service):
        self.__token_service = token_service

    def retrieve_accounts(self):
        return [AdlsAccount(str(ix)) for ix in range(10)]

    def read_file(self, account, file_path, encoding, column_sep, to_be_read_line_count):
        return [[1, 2], [2, 3]]

    def retrieve_files(self, account, folder_path):
        return [AdlsFile("path_suffix", "file_name_%d" % (ix), 1, datetime.now(), datetime.now()) for ix in range(10)]

    def retrieve_folders(self, account, folder_path):
        return [AdlsFolder("path_suffix", "folder_name_%d" % (ix), datetime.now(), datetime.now()) for ix in range(10)]