from adlmagics.magics.session.session_viewing_magic import SessionViewingMagic
from adlmagics.session_consts import *

from adlmagics.test.magic_test_base import MagicTestBase

class SessionViewingMagicTest(MagicTestBase):
    def test_execute(self):
        self.__magic.execute("", None)
        self.assertEquals([
            "Session items:",
            "  %s : %s" % (session_tenant.name, session_tenant.default_value),
            "  %s : %s" % (session_user.name, session_user.default_value),
            "  %s : %s" % (session_adla_account.name, session_adla_account.default_value),
            "  %s : %s" % (session_adls_account.name, session_adls_account.default_value),
            "  %s : %s" % (session_job_runtime.name, session_job_runtime.default_value),
            "  %s : %s" % (session_job_priority.name, session_job_priority.default_value),
            "  %s : %s" % (session_job_parallelism.name, session_job_parallelism.default_value),
            "  %s : %s" % (session_paging_numberperpage.name, session_paging_numberperpage.default_value),
            "  %s : %s" % (session_file_encoding.name, session_file_encoding.default_value)], self._presenter_factory.presented_logs)

    def setUp(self):
        super(SessionViewingMagicTest, self).setUp()

        self.__magic = SessionViewingMagic(self._session_service, self._presenter_factory)

    def tearDown(self):
        self.__magic = None

        super(SessionViewingMagicTest, self).tearDown()