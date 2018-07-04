from uuid import uuid4
from IPython.core.error import UsageError

from adlmagics.magics.adla.adla_job_viewing_magic import AdlaJobViewingMagic
from adlmagics.models.adla_job import AdlaJob
from adlmagics.exceptions import MagicArgumentError, MagicArgumentMissingError
from adlmagics.session_consts import session_adla_account, session_null_value

from adlmagics.test.adla_magic_test_base import AdlaMagicTestBase

class AdlaJobViewingMagicTest(AdlaMagicTestBase):
    adla_account = "mock_adla_account"
    job_id = str(uuid4())

    def test_execute_with_correct_arg_string(self):
        arg_string = "--account %s --job_id %s" % (AdlaJobViewingMagicTest.adla_account, AdlaJobViewingMagicTest.job_id)
        retrieved_job = self.__magic.execute(arg_string, None)
        self.__validate(retrieved_job)

    def test_execute_with_incorrect_arg_string(self):
        arg_string = "--account_1 %s --job_id %s" % (AdlaJobViewingMagicTest.adla_account, AdlaJobViewingMagicTest.job_id)
        self.assertRaises(UsageError, self.__magic.execute, arg_string, None)

        arg_string = "--account %s --job_id_1 %s" % (AdlaJobViewingMagicTest.adla_account, AdlaJobViewingMagicTest.job_id)
        self.assertRaises(UsageError, self.__magic.execute, arg_string, None)

    def test_execute_with_missing_account(self):
        # account missing in arg_string, but not in session
        arg_string = "--job_id %s" % (AdlaJobViewingMagicTest.job_id)
        self._session_service.set_session_item(session_adla_account.name, AdlaJobViewingMagicTest.adla_account)
        retrieved_job = self.__magic.execute(arg_string, None)
        self.__validate(retrieved_job)

        # account missing in both arg_string and session
        arg_string = "--job_id %s" % (AdlaJobViewingMagicTest.job_id)
        self._session_service.set_session_item(session_adla_account.name, session_null_value)
        self.assertRaises(MagicArgumentError, self.__magic.execute, arg_string, None)

    def test_execute_with_missing_job_id(self):
        arg_string = "--account %s" % (AdlaJobViewingMagicTest.adla_account)
        self.assertRaises(MagicArgumentMissingError, self.__magic.execute, arg_string, None)

    def setUp(self):
        super(AdlaJobViewingMagicTest, self).setUp()

        self.__magic = AdlaJobViewingMagic(self._session_service, self._presenter_factory, self._result_converter, self._adla_service)

    def tearDown(self):
        self.__magic = None

        super(AdlaJobViewingMagicTest, self).tearDown()

    def __validate(self, retrieved_job):
        # Verify that the magic actually returns something
        self.assertIsNotNone(retrieved_job)

        self.assertEquals([
            "Viewing azure data lake job by id '%s' under account '%s'..." % (AdlaJobViewingMagicTest.job_id, AdlaJobViewingMagicTest.adla_account),
            AdlaJob.__name__], self._presenter_factory.presented_logs)

    