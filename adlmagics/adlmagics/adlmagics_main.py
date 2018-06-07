from IPython.core.magic import Magics, magics_class, line_cell_magic
from sys import stdout
from os import linesep

from adlmagics.services.azure_token_service import AzureTokenService
from adlmagics.services.adla_service_sdk_impl import AdlaServiceSdkImpl
from adlmagics.services.adls_service_sdk_impl import AdlsServiceSdkImpl

from adlmagics.magics.azure.azure_magic_base import AzureMagicBase
from adlmagics.magics.azure.azure_login_magic import AzureLoginMagic
from adlmagics.magics.azure.azure_logout_magic import AzureLogoutMagic

from adlmagics.magics.adla.adla_magic_base import AdlaMagicBase
from adlmagics.magics.adla.adla_accounts_listing_magic import AdlaAccountsListingMagic
from adlmagics.magics.adla.adla_job_viewing_magic import AdlaJobViewingMagic
from adlmagics.magics.adla.adla_job_submission_magic import AdlaJobSubmissionMagic
from adlmagics.magics.adla.adla_jobs_listing_magic import AdlaJobsListingMagic

from adlmagics.magics.adls.adls_magic_base import AdlsMagicBase
from adlmagics.magics.adls.adls_accounts_listing_magic import AdlsAccountsListingMagic
from adlmagics.magics.adls.adls_folders_listing_magic import AdlsFoldersListingMagic
from adlmagics.magics.adls.adls_files_listing_magic import AdlsFilesListingMagic
from adlmagics.magics.adls.adls_file_sampling_magic import AdlsFileSamplingMagic

@magics_class
class AdlMagics(Magics):
    def __init__(self, shell, data = None):
        super(AdlMagics, self).__init__(shell)

        self.__magics = dict()

        self.__token_service = AzureTokenService()

        self.__adla_service = AdlaServiceSdkImpl(self.__token_service)
        self.__adls_service = AdlsServiceSdkImpl(self.__token_service)

        self.__register_azure_magic(AzureLoginMagic)
        self.__register_azure_magic(AzureLogoutMagic)

        self.__register_adla_magic(AdlaAccountsListingMagic)
        self.__register_adla_magic(AdlaJobSubmissionMagic)
        self.__register_adla_magic(AdlaJobViewingMagic)
        self.__register_adla_magic(AdlaJobsListingMagic)

        self.__register_adls_magic(AdlsAccountsListingMagic)
        self.__register_adls_magic(AdlsFoldersListingMagic)
        self.__register_adls_magic(AdlsFilesListingMagic)
        self.__register_adls_magic(AdlsFileSamplingMagic)

        self.__write_line("%s initialized" % (AdlMagics.__name__))

    @line_cell_magic
    def adl(self, line, cell = ""):
        cmd = line.strip()
        arg_string = ""
        try:
            cmd_end_index = cmd.index(" ")
            cmd = cmd[0:cmd_end_index].strip().lower()
            arg_string = line[cmd_end_index:].strip()
        except:
            pass

        if (cmd not in self.__magics):
            raise ValueError("Unsupported command '%s'" % cmd)

        magic = self.__magics[cmd]
        return magic.execute(arg_string, cell)

    def __register_azure_magic(self, azure_magic_class):
        if (not issubclass(azure_magic_class, AzureMagicBase)):
            raise TypeError("%s not a azure magic class." % (azure_magic_class.__name__))

        azure_magic = azure_magic_class(self.__token_service)
        self.__magics[azure_magic.cmd_name.lower()] = azure_magic

    def __register_adla_magic(self, adla_magic_class):
        if (not issubclass(adla_magic_class, AdlaMagicBase)):
            raise TypeError("%s not a adla magic class." % (adla_magic_class.__name__))

        adla_magic = adla_magic_class(self.__adla_service)
        self.__magics[adla_magic.cmd_name.lower()] = adla_magic

    def __register_adls_magic(self, adls_magic_class):
        if (not issubclass(adls_magic_class, AdlsMagicBase)):
            raise TypeError("%s not a adls magic class." % (adls_magic_class.__name__))

        adls_magic = adls_magic_class(self.__adls_service)
        self.__magics[adls_magic.cmd_name.lower()] = adls_magic

    def __write_line(self, text):
        stdout.write(text + linesep)