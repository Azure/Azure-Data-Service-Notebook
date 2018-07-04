from IPython.core.magic_arguments import magic_arguments, argument, parse_argstring

from adlmagics.magics.adls.adls_magic_base import AdlsMagicBase
from adlmagics.session_consts import session_adls_account

class AdlsFoldersListingMagic(AdlsMagicBase):
    def __init__(self, session_service, presenter_factory, result_converter, adls_service):
        super(AdlsFoldersListingMagic, self).__init__("liststorefolders", session_service, presenter_factory, result_converter, adls_service)

    @magic_arguments()
    @argument("--account", type = str, help = "Azure data lake store account name.")
    @argument("--folder_path", default = "", help = "Relative path of the folder whose folders are to be listed.")
    def execute(self, arg_string, content_string = None):
        args = parse_argstring(self.execute, arg_string)

        self.__validate_args(args)

        self._present("Listing azure data lake store folders under folder '%s' of account '%s'..." % (args.folder_path, args.account))

        folders = self._adls_service.retrieve_folders(args.account, args.folder_path)

        self._present("(%d) azure data lake store folder(s) listed." % (len(folders)))

        self._present(folders)

        return self._convert_result(folders)

    def __validate_args(self, args):
        self._validate_arg(args, "account", session_adls_account.name)