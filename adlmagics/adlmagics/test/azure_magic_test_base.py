from adlmagics.test.magic_test_base import MagicTestBase
from adlmagics.test.mocks.mock_token_service import MockTokenService

class AzureMagicTestBase(MagicTestBase):
    def setUp(self):
        super(AzureMagicTestBase, self).setUp()

        self._token_service = MockTokenService()

    def tearDown(self):
        self._token_service = None

        super(AzureMagicTestBase, self).tearDown()