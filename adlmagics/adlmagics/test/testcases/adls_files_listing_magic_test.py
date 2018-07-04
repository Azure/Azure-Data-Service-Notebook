from IPython.core.error import UsageError

from adlmagics.magics.adls.adls_files_listing_magic import AdlsFilesListingMagic
from adlmagics.exceptions import MagicArgumentMissingError, MagicArgumentError
from adlmagics.session_consts import session_adls_account, session_null_value
from adlmagics.models.adls_file import AdlsFile

from adlmagics.test.adls_magic_test_base import AdlsMagicTestBase

class AdlsFilesListingMagicTest(AdlsMagicTestBase):
    adls_account = "mock_adls_account"
    folder_path = "test"

    def test_execute_with_correct_arg_string(self):
        arg_string = "--account %s --folder_path %s" % (AdlsFilesListingMagicTest.adls_account, AdlsFilesListingMagicTest.folder_path)
        files = self.__magic.execute(arg_string, None)
        self.__validate(files)

    def test_execute_with_incorrect_arg_string(self):
        arg_string = "--account_1 %s --folder_path %s" % (AdlsFilesListingMagicTest.adls_account, AdlsFilesListingMagicTest.folder_path)
        self.assertRaises(UsageError, self.__magic.execute, arg_string, None)

        arg_string = "--account %s --folder_path_1 %s" % (AdlsFilesListingMagicTest.adls_account, AdlsFilesListingMagicTest.folder_path)
        self.assertRaises(UsageError, self.__magic.execute, arg_string, None)

    def test_execute_with_missing_account(self):
        # account missing in arg_string, but not in session
        arg_string = "--folder_path %s" % (AdlsFilesListingMagicTest.folder_path)
        self._session_service.set_session_item(session_adls_account.name, AdlsFilesListingMagicTest.adls_account)
        files = self.__magic.execute(arg_string, None)
        self.__validate(files)

        # account missing in both arg_string and session
        arg_string = "--folder_path %s" % (AdlsFilesListingMagicTest.folder_path)
        self._session_service.set_session_item(session_adls_account.name, session_null_value)
        self.assertRaises(MagicArgumentError, self.__magic.execute, arg_string, None)

    def test_execute_with_missing_folder_path(self):
        arg_string = "--account %s" % (AdlsFilesListingMagicTest.adls_account)
        self.assertRaises(MagicArgumentMissingError, self.__magic.execute, arg_string, None)

    def setUp(self):
        super(AdlsFilesListingMagicTest, self).setUp()

        self.__magic = AdlsFilesListingMagic(self._session_service, self._presenter_factory, self._result_converter, self._adls_service)

    def tearDown(self):
        self.__magic = None

        super(AdlsFilesListingMagicTest, self).tearDown()

    def __validate(self, files):
        # Verify that the magic actually returns something
        self.assertIsNotNone(files)

        self.assertEquals([
            "Listing azure data lake store files under folder '%s' of account '%s'..." % (AdlsFilesListingMagicTest.folder_path, AdlsFilesListingMagicTest.adls_account),
            "(%d) azure data lake store file(s) listed." % (len(files)),
            "A list of %s" % (AdlsFile.__name__)], self._presenter_factory.presented_logs)

        self._presenter_factory.clear()