from adlmagics.magics.adla.adla_accounts_listing_magic import AdlaAccountsListingMagic

from adlmagics.test.adla_magic_test_base import AdlaMagicTestBase

class AdlaAccountsListingMagicTest(AdlaMagicTestBase):
    def test_execute(self):
        adla_accounts = self.__magic.execute("", None)

        # Verify that the magic actually returns something
        self.assertIsNotNone(adla_accounts)
        
        self.assertEquals([
            "Listing azure data lake analytics accounts...",
            "(%d) azure data lake analytics account(s) listed." % (len(adla_accounts))], self._presenter_factory.presented_logs)

    def setUp(self):
        super(AdlaAccountsListingMagicTest, self).setUp()

        self.__magic = AdlaAccountsListingMagic(self._session_service, self._presenter_factory, self._result_converter, self._adla_service)

    def tearDown(self):
        self.__magic = None

        super(AdlaAccountsListingMagicTest, self).tearDown()