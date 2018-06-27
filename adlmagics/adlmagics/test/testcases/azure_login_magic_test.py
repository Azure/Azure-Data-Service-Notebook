from IPython.core.error import UsageError

from adlmagics.magics.azure.azure_login_magic import AzureLoginMagic
from adlmagics.session_consts import session_tenant, session_user
from adlmagics.exceptions import MagicArgumentMissingError

from adlmagics.test.azure_magic_test_base import AzureMagicTestBase

class AzureLoginMagicTest(AzureMagicTestBase):
    tenant = "mock_tenant"

    def test_execute_with_correct_arg_string(self):
        arg_string = "--tenant %s" % (AzureLoginMagicTest.tenant)

        self.__magic.execute(arg_string, None)

        self.assertEqual(self._session_service.get_session_item(session_tenant.name), self._token_service.tenant)
        self.assertEqual(self._session_service.get_session_item(session_user.name), self._token_service.logged_in_user)

        self.assertEquals([
            "Waiting for user login...",
            "User '%s' logged in to tenant '%s'" % (self._token_service.logged_in_user, self._token_service.tenant)], self._presenter_factory.presented_logs)

    def test_execute_with_incorrect_arg_string(self):
        arg_string = "--tenant_1 %s" % (AzureLoginMagicTest.tenant)
        self.assertRaises(UsageError, self.__magic.execute, arg_string, None)

    def test_execute_with_missing_tenant(self):
        self.assertRaises(MagicArgumentMissingError, self.__magic.execute, "", None)

    def setUp(self):
        super(AzureLoginMagicTest, self).setUp()

        self.__magic = AzureLoginMagic(self._session_service, self._presenter_factory, self._token_service)

    def tearDown(self):
        self.__magic = None

        super(AzureLoginMagicTest, self).tearDown()