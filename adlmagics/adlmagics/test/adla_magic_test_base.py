from adlmagics.test.magic_test_base import MagicTestBase
from adlmagics.test.mocks.mock_token_service import MockTokenService
from adlmagics.test.mocks.mock_adla_service import MockAdlaService

class AdlaMagicTestBase(MagicTestBase):
    def setUp(self):
        super(AdlaMagicTestBase, self).setUp()

        self._token_service = MockTokenService()
        self._adla_service = MockAdlaService(self._token_service)

    def tearDown(self):
        self._adla_service = None
        self._token_service = None

        super(AdlaMagicTestBase, self).tearDown()