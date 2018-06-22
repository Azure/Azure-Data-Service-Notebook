from IPython.core.magic import Magics, magics_class, line_cell_magic
from sys import stdout
from os import linesep
from os.path import join, expanduser

from adlmagics.version import adlmagics_version

from adlmagics.converters.matrix_to_dataframe_converter import MatrixToDataFrameConverter
from adlmagics.converters.object_to_dataframe_converter import ObjectToDataFrameConverter
from adlmagics.converters.quiet_converter import QuietConverter

from adlmagics.utils.json_file_persister import JsonFilePersister

from adlmagics.presenters.presenter_base import PresenterBase
from adlmagics.presenters.text_presenter import TextPresenter
from adlmagics.presenters.adla_job_presenter import AdlaJobPresenter
from adlmagics.presenters.adla_jobs_presenter import AdlaJobsPresenter
from adlmagics.presenters.adls_files_presenter import AdlsFilesPresenter
from adlmagics.presenters.adls_folders_presenter import AdlsFoldersPresenter

from adlmagics.services.azure_token_service import AzureTokenService
from adlmagics.services.adla_service_sdk_impl import AdlaServiceSdkImpl
from adlmagics.services.adls_service_sdk_impl import AdlsServiceSdkImpl
from adlmagics.services.session_service import SessionService
from adlmagics.services.presenter_factory import PresenterFactory

from adlmagics.magics.session.session_magic_base import SessionMagicBase
from adlmagics.magics.session.session_viewing_magic import SessionViewingMagic
from adlmagics.magics.session.session_item_setting_magic import SessionItemSettingMagic

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

        self.__session_service = SessionService(JsonFilePersister(join(expanduser("~"), "adlmagics.session"), "utf-8"))

        self.__presenter_factory = PresenterFactory()
        self.__register_presenter(TextPresenter)
        self.__register_presenter(AdlaJobPresenter)
        self.__register_presenter(AdlaJobsPresenter)
        self.__register_presenter(AdlsFilesPresenter)
        self.__register_presenter(AdlsFoldersPresenter)

        self.__token_service = AzureTokenService()
        self.__adla_service = AdlaServiceSdkImpl(self.__token_service)
        self.__adls_service = AdlsServiceSdkImpl(self.__token_service)
        
        self.__initialize_magics()

        self.__write_line("%s %s initialized" % (AdlMagics.__name__, adlmagics_version))

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

    def __register_presenter(self, presenter_class):
        if (not issubclass(presenter_class, PresenterBase)):
            raise TypeError("%s not a presenter class." % (presenter_class.__name__))

        presenter = presenter_class()
        self.__presenter_factory.register_presenter(presenter.target_type, presenter)
    
    def __initialize_magics(self):
        quiet_converter = QuietConverter()
        object_to_df_converter = ObjectToDataFrameConverter()
        matrix_to_df_converter = MatrixToDataFrameConverter()
        
        self.__magics = dict()

        self.__register_session_magic(SessionViewingMagic, quiet_converter)
        self.__register_session_magic(SessionItemSettingMagic, quiet_converter)
        
        self.__register_azure_magic(AzureLoginMagic, quiet_converter)
        self.__register_azure_magic(AzureLogoutMagic, quiet_converter)

        self.__register_adla_magic(AdlaAccountsListingMagic, object_to_df_converter)
        self.__register_adla_magic(AdlaJobSubmissionMagic, object_to_df_converter)
        self.__register_adla_magic(AdlaJobViewingMagic, object_to_df_converter)
        self.__register_adla_magic(AdlaJobsListingMagic, object_to_df_converter)

        self.__register_adls_magic(AdlsAccountsListingMagic, object_to_df_converter)
        self.__register_adls_magic(AdlsFoldersListingMagic, object_to_df_converter)
        self.__register_adls_magic(AdlsFilesListingMagic, object_to_df_converter)
        self.__register_adls_magic(AdlsFileSamplingMagic, matrix_to_df_converter())

    def __register_session_magic(self, session_magic_class, result_converter):
        if (not issubclass(session_magic_class, SessionMagicBase)):
            raise TypeError("%s not a session magic class." % (session_magic_class.__name__))

        session_magic = session_magic_class(self.__session_service, self.__presenter_factory, result_converter)
        self.__magics[session_magic.cmd_name.lower()] = session_magic
    
    def __register_azure_magic(self, azure_magic_class, result_converter):
        if (not issubclass(azure_magic_class, AzureMagicBase)):
            raise TypeError("%s not a azure magic class." % (azure_magic_class.__name__))

        azure_magic = azure_magic_class(self.__session_service, self.__presenter_factory, result_converter, self.__token_service)
        self.__magics[azure_magic.cmd_name.lower()] = azure_magic

    def __register_adla_magic(self, adla_magic_class, result_converter):
        if (not issubclass(adla_magic_class, AdlaMagicBase)):
            raise TypeError("%s not a adla magic class." % (adla_magic_class.__name__))

        adla_magic = adla_magic_class(self.__session_service, self.__presenter_factory, object_to_df_converter, self.__adla_service)
        self.__magics[adla_magic.cmd_name.lower()] = adla_magic

    def __register_adls_magic(self, adls_magic_class, result_converter):
        if (not issubclass(adls_magic_class, AdlsMagicBase)):
            raise TypeError("%s not a adls magic class." % (adls_magic_class.__name__))

        adls_magic = adls_magic_class(self.__session_service, self.__presenter_factory, result_converter, self.__adls_service)
        self.__magics[adls_magic.cmd_name.lower()] = adls_magic

    def __write_line(self, text):
        stdout.write(text + linesep)