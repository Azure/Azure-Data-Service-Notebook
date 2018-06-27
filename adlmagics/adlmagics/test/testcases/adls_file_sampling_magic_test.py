from IPython.core.error import UsageError

from adlmagics.magics.adls.adls_file_sampling_magic import AdlsFileSamplingMagic
from adlmagics.exceptions import MagicArgumentMissingError, MagicArgumentError
from adlmagics.session_consts import session_adls_account, session_file_encoding, session_null_value

from adlmagics.test.adls_magic_test_base import AdlsMagicTestBase

class AdlsFileSamplingMagicTest(AdlsMagicTestBase):
    adls_account = "mock_adls_account"
    tsv_file_path = "test/sample.tsv"
    tsv_file_type = "tsv"

    def test_execute_with_correct_arg_string(self):
        file_path = "test/sample.tsv"
        arg_string = "--account %s --file_path %s --file_type tsv --encoding utf-8 --row_number 50" % (AdlsFileSamplingMagicTest.adls_account, file_path)
        sampled_data = self.__magic.execute(arg_string, None)
        self.__validate(file_path, sampled_data)
        arg_string = "--account %s --file_path %s --encoding utf-8 --row_number 50" % (AdlsFileSamplingMagicTest.adls_account, file_path)
        sampled_data = self.__magic.execute(arg_string, None)
        self.__validate(file_path, sampled_data)

        file_path = "test/sample.csv"
        arg_string = "--account %s --file_path %s --file_type csv --encoding utf-8 --row_number 50" % (AdlsFileSamplingMagicTest.adls_account, file_path)
        sampled_data = self.__magic.execute(arg_string, None)
        self.__validate(file_path, sampled_data)
        arg_string = "--account %s --file_path %s --encoding utf-8 --row_number 50" % (AdlsFileSamplingMagicTest.adls_account, file_path)
        sampled_data = self.__magic.execute(arg_string, None)
        self.__validate(file_path, sampled_data)

        file_path = "test/sample.txt"
        arg_string = "--account %s --file_path %s --file_type txt --encoding utf-8 --row_number 50" % (AdlsFileSamplingMagicTest.adls_account, file_path)
        sampled_data = self.__magic.execute(arg_string, None)
        self.__validate(file_path, sampled_data)
        arg_string = "--account %s --file_path %s --encoding utf-8 --row_number 50" % (AdlsFileSamplingMagicTest.adls_account, file_path)
        sampled_data = self.__magic.execute(arg_string, None)
        self.__validate(file_path, sampled_data)

        file_path = "test/sample.tsv"
        arg_string = "--account %s --file_path %s --file_type tsv --encoding utf-8" % (AdlsFileSamplingMagicTest.adls_account, file_path)
        sampled_data = self.__magic.execute(arg_string, None)
        self.__validate(file_path, sampled_data)

        file_path = "test/sample.TSV"
        arg_string = "--account %s --file_path %s --encoding utf-8" % (AdlsFileSamplingMagicTest.adls_account, file_path)
        sampled_data = self.__magic.execute(arg_string, None)
        self.__validate(file_path, sampled_data)

    def test_execute_with_incorrect_arg_string(self):
        arg_string = "--account_1 %s --file_path %s --file_type %s --encoding utf-8 --row_number 50" % (AdlsFileSamplingMagicTest.adls_account, AdlsFileSamplingMagicTest.tsv_file_path, AdlsFileSamplingMagicTest.tsv_file_type)
        self.assertRaises(UsageError, self.__magic.execute, arg_string, None)

        arg_string = "--account %s --file_path_1 %s --file_type %s --encoding utf-8 --row_number 50" % (AdlsFileSamplingMagicTest.adls_account, AdlsFileSamplingMagicTest.tsv_file_path, AdlsFileSamplingMagicTest.tsv_file_type)
        self.assertRaises(UsageError, self.__magic.execute, arg_string, None)

        arg_string = "--account %s --file_path %s --file_type_1 %s --encoding utf-8 --row_number 50" % (AdlsFileSamplingMagicTest.adls_account, AdlsFileSamplingMagicTest.tsv_file_path, AdlsFileSamplingMagicTest.tsv_file_type)
        self.assertRaises(UsageError, self.__magic.execute, arg_string, None)

        arg_string = "--account %s --file_path %s --file_type %s --encoding_1 utf-8 --row_number 50" % (AdlsFileSamplingMagicTest.adls_account, AdlsFileSamplingMagicTest.tsv_file_path, AdlsFileSamplingMagicTest.tsv_file_type)
        self.assertRaises(UsageError, self.__magic.execute, arg_string, None)

        arg_string = "--account %s --file_path %s --file_type %s --encoding utf-8 --row_number_1 50" % (AdlsFileSamplingMagicTest.adls_account, AdlsFileSamplingMagicTest.tsv_file_path, AdlsFileSamplingMagicTest.tsv_file_type)
        self.assertRaises(UsageError, self.__magic.execute, arg_string, None)

        arg_string = "--account %s --file_path test/sample.tsv --file_type TSV --encoding utf-8 --row_number 50" % (AdlsFileSamplingMagicTest.adls_account)
        self.assertRaises(UsageError, self.__magic.execute, arg_string, None)

    def test_execute_with_missing_account(self):
        # account missing in arg_string, but not in session
        arg_string = "--file_path %s --file_type %s --encoding utf-8 --row_number 50" % (AdlsFileSamplingMagicTest.tsv_file_path, AdlsFileSamplingMagicTest.tsv_file_type)
        self._session_service.set_session_item(session_adls_account.name, "mock_adls_account")
        sampled_data = self.__magic.execute(arg_string, None)
        self.__validate(AdlsFileSamplingMagicTest.tsv_file_path, sampled_data)

        # account missing in both arg_string and session
        arg_string = "--file_path %s --file_type %s --encoding utf-8 --row_number 50" % (AdlsFileSamplingMagicTest.tsv_file_path, AdlsFileSamplingMagicTest.tsv_file_type)
        self._session_service.set_session_item(session_adls_account.name, session_null_value)
        self.assertRaises(MagicArgumentError, self.__magic.execute, arg_string, None)

    def test_execute_with_missing_file_path(self):
        arg_string = "--account mock_adls_account --file_type tsv --encoding utf-8 --row_number 50"
        self.assertRaises(MagicArgumentMissingError, self.__magic.execute, arg_string, None)

    def test_execute_with_missing_file_type(self):
        # missing both file_path and file_type in arg_string
        arg_string = "--account %s --encoding utf-8 --row_number 50" % (AdlsFileSamplingMagicTest.adls_account)
        self.assertRaises(MagicArgumentMissingError, self.__magic.execute, arg_string, None)

        # missing file_type and extension in file_path in arg_string
        arg_string = "--account %s --file_path test/sample --encoding utf-8 --row_number 50" % (AdlsFileSamplingMagicTest.adls_account)
        self.assertRaises(MagicArgumentMissingError, self.__magic.execute, arg_string, None)

        # unsupported file_type in arg_string
        arg_string = "--account %s --file_path test/sample.tsv --file_type tst --encoding utf-8 --row_number 50" % (AdlsFileSamplingMagicTest.adls_account)
        self.assertRaises(UsageError, self.__magic.execute, arg_string, None)

        # missing file_type and unsupported extension in file_path in arg_string
        arg_string = "--account %s --file_path test/sample.tst --encoding utf-8 --row_number 50" % (AdlsFileSamplingMagicTest.adls_account)
        self.assertRaises(MagicArgumentError, self.__magic.execute, arg_string, None)

    def test_execute_with_missing_encoding(self):
        # encoding missing in arg_string, but not in session
        arg_string = "--account %s --file_path %s --file_type %s --row_number 50" % (AdlsFileSamplingMagicTest.adls_account, AdlsFileSamplingMagicTest.tsv_file_path, AdlsFileSamplingMagicTest.tsv_file_type)
        self._session_service.set_session_item(session_file_encoding.name, "utf-8")
        sampled_data = self.__magic.execute(arg_string, None)
        self.__validate(AdlsFileSamplingMagicTest.tsv_file_path, sampled_data)

        # encoding missing in arg_string, then its default value will be used, the config in session service will be ignored.

    def test_execute_with_boundary_row_number(self):
        # Set boundary values to row_number in arg_string
        arg_string = "--account %s --file_path %s --file_type %s --row_number -1" % (AdlsFileSamplingMagicTest.adls_account, AdlsFileSamplingMagicTest.tsv_file_path, AdlsFileSamplingMagicTest.tsv_file_type)
        self.assertRaises(MagicArgumentError, self.__magic.execute, arg_string, None)

        arg_string = "--account %s --file_path %s --file_type %s --row_number 0" % (AdlsFileSamplingMagicTest.adls_account, AdlsFileSamplingMagicTest.tsv_file_path, AdlsFileSamplingMagicTest.tsv_file_type)
        self.assertRaises(MagicArgumentError, self.__magic.execute, arg_string, None)

        # row_number missing in arg_string, then its default value will be used.

    def setUp(self):
        super(AdlsFileSamplingMagicTest, self).setUp()

        self.__magic = AdlsFileSamplingMagic(self._session_service, self._presenter_factory, self._result_converter, self._adls_service)

    def tearDown(self):
        self.__magic = None

        super(AdlsFileSamplingMagicTest, self).tearDown()

    def __validate(self, file_path, sampled_data):
        # Verify that the magic actually returns something
        self.assertIsNotNone(sampled_data)

        self.assertEquals([
            "Sampling data lake store file '%s'..." % (file_path),
            "(%d) row(s) sampled." % (len(sampled_data))], self._presenter_factory.presented_logs)

        self._presenter_factory.clear()