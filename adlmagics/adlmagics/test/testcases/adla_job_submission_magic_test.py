from IPython.core.error import UsageError

from adlmagics.magics.adla.adla_job_submission_magic import AdlaJobSubmissionMagic
from adlmagics.session_consts import session_adla_account, session_job_parallelism, session_job_priority, session_job_runtime, session_null_value
from adlmagics.models.adla_job import AdlaJob
from adlmagics.exceptions import MagicArgumentError, MagicArgumentMissingError

from adlmagics.test.adla_magic_test_base import AdlaMagicTestBase
from adlmagics.test.mocks.mock_result_receiver import MockResultReceiver

class AdlaJobSubmissionMagicTest(AdlaMagicTestBase):
    adla_account = "mock_adla_account"
    job_name = "mock_job_name"
    job_script = "mock job scrpt"
    job_parallelism = 5
    job_priority = 100
    job_runtime = "mock_runtime"
    result_job = "submitted_job"
        
    def test_execute_with_correct_arg_string(self):
        arg_string = "--account %s --name %s --parallelism %d --priority %d --runtime %s --result_job %s" % (AdlaJobSubmissionMagicTest.adla_account, AdlaJobSubmissionMagicTest.job_name, AdlaJobSubmissionMagicTest.job_parallelism, AdlaJobSubmissionMagicTest.job_priority, AdlaJobSubmissionMagicTest.job_runtime, AdlaJobSubmissionMagicTest.result_job)
        self.__magic.execute(arg_string, AdlaJobSubmissionMagicTest.job_script)
        self.__validate()

    def test_execute_with_incorrect_arg_string(self):
        arg_string = "--account_1 %s --name %s --parallelism %d --priority %d --runtime %s --result_job %s" % (AdlaJobSubmissionMagicTest.adla_account, AdlaJobSubmissionMagicTest.job_name, AdlaJobSubmissionMagicTest.job_parallelism, AdlaJobSubmissionMagicTest.job_priority, AdlaJobSubmissionMagicTest.job_runtime, AdlaJobSubmissionMagicTest.result_job)
        self.assertRaises(UsageError, self.__magic.execute, arg_string, AdlaJobSubmissionMagicTest.job_script)

        arg_string = "--account %s --name_1 %s --parallelism %d --priority %d --runtime %s --result_job %s" % (AdlaJobSubmissionMagicTest.adla_account, AdlaJobSubmissionMagicTest.job_name, AdlaJobSubmissionMagicTest.job_parallelism, AdlaJobSubmissionMagicTest.job_priority, AdlaJobSubmissionMagicTest.job_runtime, AdlaJobSubmissionMagicTest.result_job)
        self.assertRaises(UsageError, self.__magic.execute, arg_string, AdlaJobSubmissionMagicTest.job_script)

        arg_string = "--account %s --name %s --parallelism_1 %d --priority %d --runtime %s --result_job %s" % (AdlaJobSubmissionMagicTest.adla_account, AdlaJobSubmissionMagicTest.job_name, AdlaJobSubmissionMagicTest.job_parallelism, AdlaJobSubmissionMagicTest.job_priority, AdlaJobSubmissionMagicTest.job_runtime, AdlaJobSubmissionMagicTest.result_job)
        self.assertRaises(UsageError, self.__magic.execute, arg_string, AdlaJobSubmissionMagicTest.job_script)

        arg_string = "--account %s --name %s --parallelism %d --priority_1 %d --runtime %s --result_job %s" % (AdlaJobSubmissionMagicTest.adla_account, AdlaJobSubmissionMagicTest.job_name, AdlaJobSubmissionMagicTest.job_parallelism, AdlaJobSubmissionMagicTest.job_priority, AdlaJobSubmissionMagicTest.job_runtime, AdlaJobSubmissionMagicTest.result_job)
        self.assertRaises(UsageError, self.__magic.execute, arg_string, AdlaJobSubmissionMagicTest.job_script)

        arg_string = "--account %s --name %s --parallelism %d --priority %d --runtime_1 %s --result_job %s" % (AdlaJobSubmissionMagicTest.adla_account, AdlaJobSubmissionMagicTest.job_name, AdlaJobSubmissionMagicTest.job_parallelism, AdlaJobSubmissionMagicTest.job_priority, AdlaJobSubmissionMagicTest.job_runtime, AdlaJobSubmissionMagicTest.result_job)
        self.assertRaises(UsageError, self.__magic.execute, arg_string, AdlaJobSubmissionMagicTest.job_script)

        arg_string = "--account %s --name %s --parallelism %d --priority %d --runtime %s --result_job_1 %s" % (AdlaJobSubmissionMagicTest.adla_account, AdlaJobSubmissionMagicTest.job_name, AdlaJobSubmissionMagicTest.job_parallelism, AdlaJobSubmissionMagicTest.job_priority, AdlaJobSubmissionMagicTest.job_runtime, AdlaJobSubmissionMagicTest.result_job)
        self.assertRaises(UsageError, self.__magic.execute, arg_string, AdlaJobSubmissionMagicTest.job_script)

    def test_execute_with_missing_account(self):
        # account missing in arg_string, but not in session
        arg_string = "--name %s --parallelism %d --priority %d --runtime %s --result_job %s" % (AdlaJobSubmissionMagicTest.job_name, AdlaJobSubmissionMagicTest.job_parallelism, AdlaJobSubmissionMagicTest.job_priority, AdlaJobSubmissionMagicTest.job_runtime, AdlaJobSubmissionMagicTest.result_job)
        self._session_service.set_session_item(session_adla_account.name, AdlaJobSubmissionMagicTest.adla_account)
        self.__magic.execute(arg_string, AdlaJobSubmissionMagicTest.job_script)
        self.__validate()

        # account missing in both arg_string and session
        arg_string = "--name %s --parallelism %d --priority %d --runtime %s" % (AdlaJobSubmissionMagicTest.job_name, AdlaJobSubmissionMagicTest.job_parallelism, AdlaJobSubmissionMagicTest.job_priority, AdlaJobSubmissionMagicTest.job_runtime)
        self._session_service.set_session_item(session_adla_account.name, session_null_value)
        self.assertRaises(MagicArgumentError, self.__magic.execute, arg_string, AdlaJobSubmissionMagicTest.job_script)

    def test_execute_with_missing_name(self):
        arg_string = "--account %s --parallelism %d --priority %d --runtime %s" % (AdlaJobSubmissionMagicTest.adla_account, AdlaJobSubmissionMagicTest.job_parallelism, AdlaJobSubmissionMagicTest.job_priority, AdlaJobSubmissionMagicTest.job_runtime)
        self.assertRaises(MagicArgumentMissingError, self.__magic.execute, arg_string, AdlaJobSubmissionMagicTest.job_script)

    def test_execute_with_missing_parallelism_in_arg_string_but_not_in_session(self):
        # parallelism missing in arg_string, but not in session
        arg_string = "--account %s --name %s --priority %d --runtime %s --result_job %s" % (AdlaJobSubmissionMagicTest.adla_account, AdlaJobSubmissionMagicTest.job_name, AdlaJobSubmissionMagicTest.job_priority, AdlaJobSubmissionMagicTest.job_runtime, AdlaJobSubmissionMagicTest.result_job)
        self._session_service.set_session_item(session_job_parallelism.name, AdlaJobSubmissionMagicTest.job_parallelism)
        self.__magic.execute(arg_string, AdlaJobSubmissionMagicTest.job_script)
        self.__validate()

        # parallelism missing both in arg_string and session
        arg_string = "--account %s --name %s --priority %d --runtime %s" % (AdlaJobSubmissionMagicTest.adla_account, AdlaJobSubmissionMagicTest.job_name, AdlaJobSubmissionMagicTest.job_priority, AdlaJobSubmissionMagicTest.job_runtime)
        self._session_service.set_session_item(session_job_parallelism.name, session_null_value)
        self.assertRaises(MagicArgumentError, self.__magic.execute, arg_string, AdlaJobSubmissionMagicTest.job_script)

    def test_execute_with_missing_priority(self):
        # priority missing in arg_string, but not in session
        arg_string = "--account %s --name %s --parallelism %d --runtime %s --result_job %s" % (AdlaJobSubmissionMagicTest.adla_account, AdlaJobSubmissionMagicTest.job_name, AdlaJobSubmissionMagicTest.job_parallelism, AdlaJobSubmissionMagicTest.job_runtime, AdlaJobSubmissionMagicTest.result_job)
        self._session_service.set_session_item(session_job_priority.name, AdlaJobSubmissionMagicTest.job_priority)
        self.__magic.execute(arg_string, AdlaJobSubmissionMagicTest.job_script)
        self.__validate()

        # priority missing in both arg_string and session
        arg_string = "--account %s --name %s --parallelism %d --runtime %s" % (AdlaJobSubmissionMagicTest.adla_account, AdlaJobSubmissionMagicTest.job_name, AdlaJobSubmissionMagicTest.job_parallelism, AdlaJobSubmissionMagicTest.job_runtime)
        self._session_service.set_session_item(session_job_priority.name, session_null_value)
        self.assertRaises(MagicArgumentError, self.__magic.execute, arg_string, AdlaJobSubmissionMagicTest.job_script)

    def test_execute_with_boundary_priority_in_arg_string(self):
        # Set boundary values to priority in arg_string
        self._session_service.set_session_item(session_job_priority.name, session_null_value)

        arg_string = "--account %s --name %s --parallelism %d --priority 0 --runtime %s" % (AdlaJobSubmissionMagicTest.adla_account, AdlaJobSubmissionMagicTest.job_name, AdlaJobSubmissionMagicTest.job_parallelism, AdlaJobSubmissionMagicTest.job_runtime)
        self.assertRaises(MagicArgumentError, self.__magic.execute, arg_string, AdlaJobSubmissionMagicTest.job_script)
        
        arg_string = "--account %s --name %s --parallelism %d --priority 1 --runtime %s --result_job %s" % (AdlaJobSubmissionMagicTest.adla_account, AdlaJobSubmissionMagicTest.job_name, AdlaJobSubmissionMagicTest.job_parallelism, AdlaJobSubmissionMagicTest.job_runtime, AdlaJobSubmissionMagicTest.result_job)
        self.__magic.execute(arg_string, AdlaJobSubmissionMagicTest.job_script)
        self.__validate()
        
        arg_string = "--account %s --name %s --parallelism %d --priority 1000 --runtime %s --result_job %s" % (AdlaJobSubmissionMagicTest.adla_account, AdlaJobSubmissionMagicTest.job_name, AdlaJobSubmissionMagicTest.job_parallelism, AdlaJobSubmissionMagicTest.job_runtime, AdlaJobSubmissionMagicTest.result_job)
        self.__magic.execute(arg_string, AdlaJobSubmissionMagicTest.job_script)
        self.__validate()

        arg_string = "--account %s --name %s --parallelism %d --priority 1001 --runtime %s" % (AdlaJobSubmissionMagicTest.adla_account, AdlaJobSubmissionMagicTest.job_name, AdlaJobSubmissionMagicTest.job_parallelism, AdlaJobSubmissionMagicTest.job_runtime)
        self.assertRaises(MagicArgumentError, self.__magic.execute, arg_string, AdlaJobSubmissionMagicTest.job_script)

        # priority missing in arg_string, set boundary values to priority in session
        arg_string = "--account %s --name %s --parallelism %d --runtime %s --result_job %s" % (AdlaJobSubmissionMagicTest.adla_account, AdlaJobSubmissionMagicTest.job_name, AdlaJobSubmissionMagicTest.job_parallelism, AdlaJobSubmissionMagicTest.job_runtime, AdlaJobSubmissionMagicTest.result_job)

        self._session_service.set_session_item(session_job_priority.name, 0)
        self.assertRaises(MagicArgumentError, self.__magic.execute, arg_string, AdlaJobSubmissionMagicTest.job_script)

        self._session_service.set_session_item(session_job_priority.name, 1)
        self.__magic.execute(arg_string, AdlaJobSubmissionMagicTest.job_script)
        self.__validate()

        self._session_service.set_session_item(session_job_priority.name, 1000)
        self.__magic.execute(arg_string, AdlaJobSubmissionMagicTest.job_script)
        self.__validate()

        self._session_service.set_session_item(session_job_priority.name, 1001)
        self.assertRaises(MagicArgumentError, self.__magic.execute, arg_string, AdlaJobSubmissionMagicTest.job_script)

    def test_execute_with_missing_runtime(self):
        # runtime missing in arg_string, but not in session
        arg_string = "--account %s --name %s --parallelism %d --priority %d --result_job %s" % (AdlaJobSubmissionMagicTest.adla_account, AdlaJobSubmissionMagicTest.job_name, AdlaJobSubmissionMagicTest.job_parallelism, AdlaJobSubmissionMagicTest.job_priority, AdlaJobSubmissionMagicTest.result_job)
        self._session_service.set_session_item(session_job_runtime.name, AdlaJobSubmissionMagicTest.job_runtime)
        self.__magic.execute(arg_string, AdlaJobSubmissionMagicTest.job_script)
        self.__validate()

        # runtime missing in both arg_string and session
        arg_string = "--account %s --name %s --parallelism %d --priority %d" % (AdlaJobSubmissionMagicTest.adla_account, AdlaJobSubmissionMagicTest.job_name, AdlaJobSubmissionMagicTest.job_parallelism, AdlaJobSubmissionMagicTest.job_priority)
        self._session_service.set_session_item(session_job_runtime.name, session_null_value)
        self.assertRaises(MagicArgumentError, self.__magic.execute, arg_string, AdlaJobSubmissionMagicTest.job_script)

    def test_execute_with_missing_result_job(self):
        arg_string = "--account %s --name %s --parallelism %d --priority %d --runtime %s" % (AdlaJobSubmissionMagicTest.adla_account, AdlaJobSubmissionMagicTest.job_name, AdlaJobSubmissionMagicTest.job_parallelism, AdlaJobSubmissionMagicTest.job_priority, AdlaJobSubmissionMagicTest.job_runtime)
        self.__magic.execute(arg_string, AdlaJobSubmissionMagicTest.job_script)
        self.assertIsNone(self.__result_receiver.last_received_result_name)
        self.assertIsNone(self.__result_receiver.last_received_result_value)

    def setUp(self):
        super(AdlaJobSubmissionMagicTest, self).setUp()

        self.__result_receiver = MockResultReceiver()
        self.__magic = AdlaJobSubmissionMagic(self._session_service, self._presenter_factory, self._result_converter, self.__result_receiver, self._adla_service)

    def tearDown(self):
        self.__magic = None
        self.__result_receiver = None

        super(AdlaJobSubmissionMagicTest, self).tearDown()

    def __validate(self):
        # Verify that the magic actually returns something
        self.assertIsNotNone(self.__result_receiver.last_received_result_name)
        self.assertEqual(self.__result_receiver.last_received_result_name, AdlaJobSubmissionMagicTest.result_job)
        self.assertIsNotNone(self.__result_receiver.last_received_result_value)

        self.assertEquals([
            "Submitting azure data lake job to account '%s'..." % (AdlaJobSubmissionMagicTest.adla_account),
            "Job submitted.",
            AdlaJob.__name__], self._presenter_factory.presented_logs)

        self._presenter_factory.clear()