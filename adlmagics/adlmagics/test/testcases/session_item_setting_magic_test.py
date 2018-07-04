from IPython.core.error import UsageError

from adlmagics.magics.session.session_item_setting_magic import SessionItemSettingMagic
from adlmagics.session_consts import session_adla_account, session_null_value
from adlmagics.exceptions import MagicArgumentMissingError, MagicArgumentError

from adlmagics.test.magic_test_base import MagicTestBase

class SessionItemSettingMagicTest(MagicTestBase):
    session_item_name = session_adla_account.name
    session_item_new_value = "mock_adla_account"

    def test_execute_with_correct_arg_string(self):
        arg_string = "--name %s --value %s" % (SessionItemSettingMagicTest.session_item_name, SessionItemSettingMagicTest.session_item_new_value)
        self.__magic.execute(arg_string, None)
        self.assertEqual(self._session_service.get_session_item(SessionItemSettingMagicTest.session_item_name), SessionItemSettingMagicTest.session_item_new_value)
        self.assertEquals(["%s set to %s" % (SessionItemSettingMagicTest.session_item_name, SessionItemSettingMagicTest.session_item_new_value)], self._presenter_factory.presented_logs)

        arg_string = "--name %s" % (SessionItemSettingMagicTest.session_item_name)
        self.__magic.execute(arg_string, None)
        self.assertEqual(self._session_service.get_session_item(SessionItemSettingMagicTest.session_item_name), session_null_value)

    def test_execute_with_incorrect_arg_string(self):
        arg_string = "--name_1 %s --value %s" % (SessionItemSettingMagicTest.session_item_name, SessionItemSettingMagicTest.session_item_new_value)
        self.assertRaises(UsageError, self.__magic.execute, arg_string, None)

        arg_string = "--name %s --value_1 %s" % (SessionItemSettingMagicTest.session_item_name, SessionItemSettingMagicTest.session_item_new_value)
        self.assertRaises(UsageError, self.__magic.execute, arg_string, None)

    def test_execute_with_missing_name(self):
        self.assertRaises(MagicArgumentMissingError, self.__magic.execute, "", None)

    def test_execute_with_boundary_name(self):
        self.assertRaises(MagicArgumentError, self.__magic.execute, "--name mock_session_item_name --value new_value", None)

    def setUp(self):
        super(SessionItemSettingMagicTest, self).setUp()

        self.__magic = SessionItemSettingMagic(self._session_service, self._presenter_factory)

    def tearDown(self):
        self.__magic = None

        super(SessionItemSettingMagicTest, self).tearDown()