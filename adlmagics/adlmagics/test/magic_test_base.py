import unittest

from adlmagics.test.mocks.mock_json_persister import MockJsonPersister
from adlmagics.test.mocks.mock_session_service import MockSessionService
from adlmagics.test.mocks.mock_presenter_factory import MockPresenterFactory
from adlmagics.test.mocks.mock_result_converter import MockResultConverter

class MagicTestBase(unittest.TestCase):
    def setUp(self):
        self._json_persister = MockJsonPersister()
        self._session_service = MockSessionService(self._json_persister)
        self._presenter_factory = MockPresenterFactory()
        self._result_converter = MockResultConverter()

    def tearDown(self):
        self._json_persister = None
        self._session_service = None
        self._presenter_factory = None
        self._result_converter = None