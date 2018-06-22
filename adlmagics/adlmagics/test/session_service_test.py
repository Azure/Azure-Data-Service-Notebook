import unittest
from os import remove

from adlmagics.services.session_service import SessionService
from adlmagics.session_consts import *

from adlmagics.test.json_mem_persister import JsonMemPersister

class SessionServiceTest(unittest.TestCase):
    def test_get_session_item_post_initialization(self):
        self.assertEqual(self.__session_service.get_session_item(session_tenant.name), session_tenant.default_value)
        self.assertEqual(self.__session_service.get_session_item(session_user.name), session_user.default_value)

        self.assertEqual(self.__session_service.get_session_item(session_adla_account.name), session_adla_account.default_value)

        self.assertEqual(self.__session_service.get_session_item(session_adls_account.name), session_adls_account.default_value)

        self.assertEqual(self.__session_service.get_session_item(session_job_runtime.name), session_job_runtime.default_value)
        self.assertEqual(self.__session_service.get_session_item(session_job_priority.name), session_job_priority.default_value)
        self.assertEqual(self.__session_service.get_session_item(session_job_parallelism.name), session_job_parallelism.default_value)

        self.assertEqual(self.__session_service.get_session_item(session_paging_numberperpage.name), session_paging_numberperpage.default_value)

        self.assertEqual(self.__session_service.get_session_item(session_file_encoding.name), session_file_encoding.default_value)

    def test_get_session_item_exceptional(self):
        self.assertEqual(self.__session_service.get_session_item("nonexisted_session_item_name"), session_null_value)
        self.assertEqual(self.__session_service.get_session_item(""), session_null_value)
        self.assertEqual(self.__session_service.get_session_item(None), session_null_value)

    def test_set_session_item(self):
        self.__session_service.set_session_item(session_tenant.name, "test tenant")
        self.assertEqual(self.__session_service.get_session_item(session_tenant.name), "test tenant")

    def test_set_session_item_exceptional(self):
        self.__session_service.set_session_item("nonexisted_session_item_name", "test value")
        self.__session_service.set_session_item("", "test value")
        self.__session_service.set_session_item(None, "test value")

    def test_session_item_names(self):
        self.assertEquals(self.__session_service.session_item_names, [
            session_tenant.name,
            session_user.name,

            session_adla_account.name,

            session_adls_account.name,

            session_job_runtime.name,
            session_job_priority.name,
            session_job_parallelism.name,

            session_paging_numberperpage.name,

            session_file_encoding.name
        ])

    
    def setUp(self):
        self.__session_service = SessionService(JsonMemPersister())

    def tearDown(self):
        self.__session_service = None