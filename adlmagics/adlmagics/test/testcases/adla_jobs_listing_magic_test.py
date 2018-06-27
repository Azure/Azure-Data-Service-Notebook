from IPython.core.error import UsageError

from adlmagics.magics.adla.adla_jobs_listing_magic import AdlaJobsListingMagic
from adlmagics.session_consts import session_adla_account, session_paging_numberperpage, session_null_value
from adlmagics.exceptions import MagicArgumentError
from adlmagics.models.adla_job import AdlaJob

from adlmagics.test.testcases.adla_magic_test_base import AdlaMagicTestBase

class AdlaJobsListingMagicTest(AdlaMagicTestBase):
    adla_account = "mock_adla_account"
    page_job_number = 10

    def test_execute_with_correct_arg_string(self):
        arg_string = "--account %s --my --page_index 0 --page_job_number %d" % (AdlaJobsListingMagicTest.adla_account, AdlaJobsListingMagicTest.page_job_number)
        jobs = self.__magic.execute(arg_string, None)
        self.__validate(jobs)
        self._presenter_factory.clear()

        arg_string = "--account %s --page_index 0 --page_job_number %d" % (AdlaJobsListingMagicTest.adla_account, AdlaJobsListingMagicTest.page_job_number)
        jobs = self.__magic.execute(arg_string, None)
        self.__validate(jobs)
        self._presenter_factory.clear()

        arg_string = "--account %s" % (AdlaJobsListingMagicTest.adla_account)
        jobs = self.__magic.execute(arg_string, None)
        self.__validate(jobs)

    def test_execute_with_incorrect_arg_string(self):
        arg_string = "--account_1 %s --my --page_index 0 --page_job_number %d" % (AdlaJobsListingMagicTest.adla_account, AdlaJobsListingMagicTest.page_job_number)
        self.assertRaises(UsageError, self.__magic.execute, arg_string, None)

        arg_string = "--account %s --my_1 --page_index 0 --page_job_number %d" % (AdlaJobsListingMagicTest.adla_account, AdlaJobsListingMagicTest.page_job_number)
        self.assertRaises(UsageError, self.__magic.execute, arg_string, None)

        arg_string = "--account %s --my --page_index_1 0 --page_job_number %d" % (AdlaJobsListingMagicTest.adla_account, AdlaJobsListingMagicTest.page_job_number)
        self.assertRaises(UsageError, self.__magic.execute, arg_string, None)

        arg_string = "--account %s --my --page_index 0 --page_job_number_1 %d" % (AdlaJobsListingMagicTest.adla_account, AdlaJobsListingMagicTest.page_job_number)
        self.assertRaises(UsageError, self.__magic.execute, arg_string, None)

    def test_execute_with_missing_account(self):
        # account missing in arg_string, but not in session
        arg_string = "--my --page_index 0 --page_job_number %d" % (AdlaJobsListingMagicTest.page_job_number)
        self._session_service.set_session_item(session_adla_account.name, AdlaJobsListingMagicTest.adla_account)
        jobs = self.__magic.execute(arg_string, None)
        self.__validate(jobs)

        # account missing in both arg_string and session
        arg_string = "--my --page_index 0 --page_job_number %d" % (AdlaJobsListingMagicTest.page_job_number)
        self._session_service.set_session_item(session_adla_account.name, session_null_value)
        self.assertRaises(MagicArgumentError, self.__magic.execute, arg_string, None)

    def test_execute_with_boundary_page_index(self):
        arg_string = "--account %s --my --page_index -1 --page_job_number %d" % (AdlaJobsListingMagicTest.adla_account, AdlaJobsListingMagicTest.page_job_number)
        self.assertRaises(MagicArgumentError, self.__magic.execute, arg_string, None)

    def test_execute_with_boundary_page_job_number(self):
        # Set boundary values to page_job_number in arg_string
        self._session_service.set_session_item(session_paging_numberperpage.name, session_null_value)

        arg_string = "--account %s --my --page_index 0 --page_job_number 0" % (AdlaJobsListingMagicTest.adla_account)
        self.assertRaises(MagicArgumentError, self.__magic.execute, arg_string, None)

        arg_string = "--account %s --my --page_index 0 --page_job_number -1" % (AdlaJobsListingMagicTest.adla_account)
        self.assertRaises(MagicArgumentError, self.__magic.execute, arg_string, None)

        # page_job_number missing in arg_string, then its default value will be used, the config in session service will be ignored.

    def setUp(self):
        super(AdlaJobsListingMagicTest, self).setUp()

        self.__magic = AdlaJobsListingMagic(self._session_service, self._presenter_factory, self._result_converter, self._adla_service)

    def tearDown(self):
        self.__magic = None

        super(AdlaJobsListingMagicTest, self).tearDown()

    def __validate(self, jobs):
        # Verify that the magic actually returns something
        self.assertIsNotNone(jobs)

        self.assertEquals([
            "Listing azure data lake jobs under account '%s'..." % (AdlaJobsListingMagicTest.adla_account),
            "(%d) azure data lake job(s) listed." % (len(jobs)),
            "A list of %s" % (AdlaJob.__name__)], self._presenter_factory.presented_logs)
