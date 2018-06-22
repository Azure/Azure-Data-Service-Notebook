from adlmagics.magics.adls.adls_magic_base import AdlsMagicBase

class AdlsAccountsListingMagic(AdlsMagicBase):
    def __init__(self, session_service, presenter_factory, result_converter, adls_service):
        super(AdlsAccountsListingMagic, self).__init__("liststoreaccounts", session_service, presenter_factory, result_converter, adls_service)

    def execute(self, arg_string, content_string):
        self._present("Listing azure data lake store accounts...")

        adls_acounts = self._adls_service.retrieve_accounts()

        self._present("(%d) azure data lake store account(s) listed." % (len(adls_acounts)))
        
        return self._convert_result(adls_acounts)