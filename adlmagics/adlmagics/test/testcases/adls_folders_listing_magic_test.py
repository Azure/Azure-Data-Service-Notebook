from IPython.core.error import UsageError

from adlmagics.magics.adls.adls_folders_listing_magic import AdlsFoldersListingMagic
from adlmagics.exceptions import MagicArgumentError
from adlmagics.session_consts import session_adls_account, session_null_value
from adlmagics.models.adls_folder import AdlsFolder

from adlmagics.test.adls_magic_test_base import AdlsMagicTestBase

class AdlsFoldersListingMagicTest(AdlsMagicTestBase):
    adls_account = "mock_adls_account"
    folder_path = "test"

    def test_execute_with_correct_arg_string(self):
        arg_string = "--account %s --folder_path %s" % (AdlsFoldersListingMagicTest.adls_account, AdlsFoldersListingMagicTest.folder_path)
        folders = self.__magic.execute(arg_string, None)
        self.__validate(AdlsFoldersListingMagicTest.folder_path, folders)

        arg_string = "--account %s" % (AdlsFoldersListingMagicTest.adls_account)
        folders = self.__magic.execute(arg_string, None)
        self.__validate("", folders)

    def test_execute_with_incorrect_arg_string(self):
        arg_string = "--account_1 %s --folder_path %s" % (AdlsFoldersListingMagicTest.adls_account, AdlsFoldersListingMagicTest.folder_path)
        self.assertRaises(UsageError, self.__magic.execute, arg_string, None)

        arg_string = "--account %s --folder_path_1 %s" % (AdlsFoldersListingMagicTest.adls_account, AdlsFoldersListingMagicTest.folder_path)
        self.assertRaises(UsageError, self.__magic.execute, arg_string, None)

    def test_execute_with_missing_account(self):
        # account missing in arg_string, but not in session
        arg_string = "--folder_path %s" % (AdlsFoldersListingMagicTest.folder_path)
        self._session_service.set_session_item(session_adls_account.name, AdlsFoldersListingMagicTest.adls_account)
        folders = self.__magic.execute(arg_string, None)
        self.__validate(AdlsFoldersListingMagicTest.folder_path, folders)

        # account missing in both arg_string and session
        arg_string = "--folder_path %s" % (AdlsFoldersListingMagicTest.folder_path)
        self._session_service.set_session_item(session_adls_account.name, session_null_value)
        self.assertRaises(MagicArgumentError, self.__magic.execute, arg_string, None)

    def setUp(self):
        super(AdlsFoldersListingMagicTest, self).setUp()

        self.__magic = AdlsFoldersListingMagic(self._session_service, self._presenter_factory, self._result_converter, self._adls_service)

    def tearDown(self):
        self.__magic = None

        super(AdlsFoldersListingMagicTest, self).tearDown()

    def __validate(self, folder_path, folders):
        # Verify that the magic actually returns something
        self.assertIsNotNone(folders)

        self.assertEquals([
            "Listing azure data lake store folders under folder '%s' of account '%s'..." % (folder_path, AdlsFoldersListingMagicTest.adls_account),
            "(%d) azure data lake store folder(s) listed." % (len(folders)),
            "A list of %s" % (AdlsFolder.__name__)], self._presenter_factory.presented_logs)

        self._presenter_factory.clear()
