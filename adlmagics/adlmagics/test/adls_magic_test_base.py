from adlmagics.test.magic_test_base import MagicTestBase
from adlmagics.test.mocks.mock_token_service import MockTokenService
from adlmagics.test.mocks.mock_adls_service import MockAdlsService

class AdlsMagicTestBase(MagicTestBase):
    def setUp(self):
        super(AdlsMagicTestBase, self).setUp()

        self._token_service = MockTokenService()
        self._adls_service = MockAdlsService(self._token_service)

    def tearDown(self):
        self._adls_service = None
        self._token_service = None

        super(AdlsMagicTestBase, self).tearDown()