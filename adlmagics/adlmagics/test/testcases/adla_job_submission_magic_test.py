from adlmagics.magics.adla.adla_job_submission_magic import AdlaJobSubmissionMagic
from adlmagics.session_consts import session_adla_account, session_job_parallelism, session_job_priority, session_job_runtime, session_null_value
from adlmagics.models.adla_job import AdlaJob
from adlmagics.exceptions import MagicArgumentError, MagicArgumentMissingError

from adlmagics.test.testcases.adla_magic_test_base import AdlaMagicTestBase

class AdlaJobSubmissionMagicTest(AdlaMagicTestBase):
    adla_account = "mock_adla_account"
    job_name = "mock_job_name"
    job_parallelism = 5
    job_priority = 100
    job_runtime = "mock_runtime"
        
    def test_execute_with_complete_arg_string(self):
        arg_string = "--account %s --name %s --parallelism %d --priority %d --runtime %s" % (AdlaJobSubmissionMagicTest.adla_account, AdlaJobSubmissionMagicTest.job_name, AdlaJobSubmissionMagicTest.job_parallelism, AdlaJobSubmissionMagicTest.job_priority, AdlaJobSubmissionMagicTest.job_runtime)
        submitted_job = self.__magic.execute(arg_string, None)
        self.__validate(submitted_job)

    def test_execute_with_missing_account_in_arg_string_but_not_in_session(self):
        arg_string = "--name %s --parallelism %d --priority %d --runtime %s" % (AdlaJobSubmissionMagicTest.job_name, AdlaJobSubmissionMagicTest.job_parallelism, AdlaJobSubmissionMagicTest.job_priority, AdlaJobSubmissionMagicTest.job_runtime)
        self._session_service.set_session_item(session_adla_account.name, AdlaJobSubmissionMagicTest.adla_account)
        submitted_job = self.__magic.execute(arg_string, None)
        self.__validate(submitted_job)

    def test_execute_with_missing_account_in_both_arg_string_and_session(self):
        arg_string = "--name %s --parallelism %d --priority %d --runtime %s" % (AdlaJobSubmissionMagicTest.job_name, AdlaJobSubmissionMagicTest.job_parallelism, AdlaJobSubmissionMagicTest.job_priority, AdlaJobSubmissionMagicTest.job_runtime)
        self._session_service.set_session_item(session_adla_account.name, session_null_value)
        self.assertRaises(MagicArgumentError, self.__magic.execute, arg_string, None)

    def test_execute_with_missing_name_in_arg_strng(self):
        arg_string = "--account %s --parallelism %d --priority %d --runtime %s" % (AdlaJobSubmissionMagicTest.adla_account, AdlaJobSubmissionMagicTest.job_parallelism, AdlaJobSubmissionMagicTest.job_priority, AdlaJobSubmissionMagicTest.job_runtime)
        self.assertRaises(MagicArgumentMissingError, self.__magic.execute, arg_string, None)

    def test_execute_with_missing_parallelism_in_arg_string_but_not_in_session(self):
        arg_string = "--account %s --name %s --priority %d --runtime %s" % (AdlaJobSubmissionMagicTest.adla_account, AdlaJobSubmissionMagicTest.job_name, AdlaJobSubmissionMagicTest.job_priority, AdlaJobSubmissionMagicTest.job_runtime)
        self._session_service.set_session_item(session_job_parallelism.name, AdlaJobSubmissionMagicTest.job_parallelism)
        submitted_job = self.__magic.execute(arg_string, None)
        self.__validate(submitted_job)

    def test_execute_with_missing_parallelism_in_both_arg_string_and_session(self):
        arg_string = "--account %s --name %s --priority %d --runtime %s" % (AdlaJobSubmissionMagicTest.adla_account, AdlaJobSubmissionMagicTest.job_name, AdlaJobSubmissionMagicTest.job_priority, AdlaJobSubmissionMagicTest.job_runtime)
        self._session_service.set_session_item(session_job_parallelism.name, session_null_value)
        self.assertRaises(MagicArgumentError, self.__magic.execute, arg_string, None)

    def test_execute_with_missing_priority_in_arg_string_but_not_in_session(self):
        arg_string = "--account %s --name %s --parallelism %d --runtime %s" % (AdlaJobSubmissionMagicTest.adla_account, AdlaJobSubmissionMagicTest.job_name, AdlaJobSubmissionMagicTest.job_parallelism, AdlaJobSubmissionMagicTest.job_runtime)
        self._session_service.set_session_item(session_job_priority.name, AdlaJobSubmissionMagicTest.job_priority)
        submitted_job = self.__magic.execute(arg_string, None)
        self.__validate(submitted_job)

    def test_execute_with_missing_priority_in_both_arg_string_and_session(self):
        arg_string = "--account %s --name %s --parallelism %d --runtime %s" % (AdlaJobSubmissionMagicTest.adla_account, AdlaJobSubmissionMagicTest.job_name, AdlaJobSubmissionMagicTest.job_parallelism, AdlaJobSubmissionMagicTest.job_runtime)
        self._session_service.set_session_item(session_job_priority.name, session_null_value)
        self.assertRaises(MagicArgumentError, self.__magic.execute, arg_string, None)

    def test_execute_with_boundary_priority_in_arg_string(self):
        self._session_service.set_session_item(session_job_priority.name, session_null_value)

        # priority : 0
        arg_string = "--account %s --name %s --parallelism %d --priority %d --runtime %s" % (AdlaJobSubmissionMagicTest.adla_account, AdlaJobSubmissionMagicTest.job_name, AdlaJobSubmissionMagicTest.job_parallelism, 0, AdlaJobSubmissionMagicTest.job_runtime)
        self.assertRaises(MagicArgumentError, self.__magic.execute, arg_string, None)

        # priority : 1
        arg_string = "--account %s --name %s --parallelism %d --priority %d --runtime %s" % (AdlaJobSubmissionMagicTest.adla_account, AdlaJobSubmissionMagicTest.job_name, AdlaJobSubmissionMagicTest.job_parallelism, 1, AdlaJobSubmissionMagicTest.job_runtime)
        submitted_job = self.__magic.execute(arg_string, None)
        self.assertEqual(1, submitted_job.priority)

        # priority : 1000
        arg_string = "--account %s --name %s --parallelism %d --priority %d --runtime %s" % (AdlaJobSubmissionMagicTest.adla_account, AdlaJobSubmissionMagicTest.job_name, AdlaJobSubmissionMagicTest.job_parallelism, 1000, AdlaJobSubmissionMagicTest.job_runtime)
        submitted_job = self.__magic.execute(arg_string, None)
        self.assertEqual(1000, submitted_job.priority)

        # priority : 1001
        arg_string = "--account %s --name %s --parallelism %d --priority %d --runtime %s" % (AdlaJobSubmissionMagicTest.adla_account, AdlaJobSubmissionMagicTest.job_name, AdlaJobSubmissionMagicTest.job_parallelism, 1001, AdlaJobSubmissionMagicTest.job_runtime)
        self.assertRaises(MagicArgumentError, self.__magic.execute, arg_string, None)

    def test_execute_with_missing_runtime_in_arg_string_but_not_in_session(self):
        arg_string = "--account %s --name %s --parallelism %d --priority %d" % (AdlaJobSubmissionMagicTest.adla_account, AdlaJobSubmissionMagicTest.job_name, AdlaJobSubmissionMagicTest.job_parallelism, AdlaJobSubmissionMagicTest.job_priority)
        self._session_service.set_session_item(session_job_runtime.name, AdlaJobSubmissionMagicTest.job_runtime)
        submitted_job = self.__magic.execute(arg_string, None)
        self.__validate(submitted_job)

    def test_execute_with_missing_priority_in_both_arg_string_and_session(self):
        arg_string = "--account %s --name %s --parallelism %d --priority %d" % (AdlaJobSubmissionMagicTest.adla_account, AdlaJobSubmissionMagicTest.job_name, AdlaJobSubmissionMagicTest.job_parallelism, AdlaJobSubmissionMagicTest.job_priority)
        self._session_service.set_session_item(session_job_runtime.name, session_null_value)
        self.assertRaises(MagicArgumentError, self.__magic.execute, arg_string, None)

    def setUp(self):
        super(AdlaJobSubmissionMagicTest, self).setUp()

        self.__magic = AdlaJobSubmissionMagic(self._session_service, self._presenter_factory, self._result_converter, self._adla_service)

    def __validate(self, submitted_job):
        # Verify that the magic actually returns something
        self.assertIsNotNone(submitted_job)

        self.assertEquals([
            "Submitting azure data lake job to account '%s'..." % (AdlaJobSubmissionMagicTest.adla_account),
            "Job submitted.",
            AdlaJob.__name__], self._presenter_factory.presented_logs)