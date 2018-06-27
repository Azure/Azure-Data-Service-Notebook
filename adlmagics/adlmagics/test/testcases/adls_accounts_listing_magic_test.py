from adlmagics.magics.adls.adls_accounts_listing_magic import AdlsAccountsListingMagic

from adlmagics.test.adls_magic_test_base import AdlsMagicTestBase

class AdlsAccountsListingMagicTest(AdlsMagicTestBase):
    def test_execute(self):
        adls_accounts = self.__magic.execute("", None)

        # Verify that the magic actually returns something
        self.assertIsNotNone(adls_accounts)
        
        self.assertEquals([
            "Listing azure data lake store accounts...",
            "(%d) azure data lake store account(s) listed." % (len(adls_accounts))], self._presenter_factory.presented_logs)

    def setUp(self):
        super(AdlsAccountsListingMagicTest, self).setUp()

        self.__magic = AdlsAccountsListingMagic(self._session_service, self._presenter_factory, self._result_converter, self._adls_service)

    def tearDown(self):
        self.__magic = None

        super(AdlsAccountsListingMagicTest, self).tearDown()