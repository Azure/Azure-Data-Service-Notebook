from adlmagics.magics.azure.azure_logout_magic import AzureLogoutMagic
from adlmagics.session_consts import session_tenant, session_user, session_null_value

from adlmagics.test.azure_magic_test_base import AzureMagicTestBase

class AzureLogoutMagicMagicTest(AzureMagicTestBase):
    def test_execute_with_correct_arg_string(self):
        tenant = self._token_service.tenant
        user = self._token_service.logged_in_user

        self.__magic.execute("", None)

        self.assertEqual(self._session_service.get_session_item(session_tenant.name), session_null_value)
        self.assertEqual(self._session_service.get_session_item(session_user.name), session_null_value)

        self.assertEquals(["User '%s' logged out of tenant '%s'" % (user, tenant)], self._presenter_factory.presented_logs)

    def setUp(self):
        super(AzureLogoutMagicMagicTest, self).setUp()

        self.__magic = AzureLogoutMagic(self._session_service, self._presenter_factory, self._token_service)

    def tearDown(self):
        self.__magic = None

        super(AzureLogoutMagicMagicTest, self).tearDown()