from uuid import uuid4

from adlmagics.magics.adla.adla_job_viewing_magic import AdlaJobViewingMagic
from adlmagics.models.adla_job import AdlaJob
from adlmagics.exceptions import MagicArgumentError, MagicArgumentMissingError
from adlmagics.session_consts import session_adla_account, session_null_value

from adlmagics.test.testcases.adla_magic_test_base import AdlaMagicTestBase

class AdlaJobViewingMagicTest(AdlaMagicTestBase):
    adla_account = "mock_adla_account"
    job_id = str(uuid4())

    def test_execute_with_complete_arg_string(self):
        arg_string = "--account %s --job_id %s" % (AdlaJobViewingMagicTest.adla_account, AdlaJobViewingMagicTest.job_id)
        retrieved_job = self.__magic.execute(arg_string, None)
        self.__validate(retrieved_job)

    def test_execute_with_missing_account_in_arg_string_but_not_in_session(self):
        arg_string = "--job_id %s" % (AdlaJobViewingMagicTest.job_id)
        self._session_service.set_session_item(session_adla_account.name, AdlaJobViewingMagicTest.adla_account)
        retrieved_job = self.__magic.execute(arg_string, None)
        self.__validate(retrieved_job)

    def test_execute_with_missing_account_in_both_arg_string_and_session(self):
        arg_string = "--job_id %s" % (AdlaJobViewingMagicTest.job_id)
        self._session_service.set_session_item(session_adla_account.name, session_null_value)
        self.assertRaises(MagicArgumentError, self.__magic.execute, arg_string, None)

    def test_execute_with_missing_job_id_in_arg_strng(self):
        arg_string = "--account %s" % (AdlaJobViewingMagicTest.adla_account)
        self.assertRaises(MagicArgumentMissingError, self.__magic.execute, arg_string, None)

    def setUp(self):
        super(AdlaJobViewingMagicTest, self).setUp()

        self.__magic = AdlaJobViewingMagic(self._session_service, self._presenter_factory, self._result_converter, self._adla_service)

    def __validate(self, retrieved_job):
        # Verify that the magic actually returns something
        self.assertIsNotNone(retrieved_job)

        self.assertEquals([
            "Viewing azure data lake job by id '%s' under account '%s'..." % (AdlaJobViewingMagicTest.job_id, AdlaJobViewingMagicTest.adla_account),
            AdlaJob.__name__], self._presenter_factory.presented_logs)

    