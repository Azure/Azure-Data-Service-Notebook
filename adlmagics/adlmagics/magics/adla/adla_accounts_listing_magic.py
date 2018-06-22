from adlmagics.magics.adla.adla_magic_base import AdlaMagicBase

class AdlaAccountsListingMagic(AdlaMagicBase):
    def __init__(self, session_service, presenter_factory, result_converter, adla_service):
        super(AdlaAccountsListingMagic, self).__init__("listaccounts", session_service, presenter_factory, result_converter, adla_service)

    def execute(self, arg_string, content_string):
        self._present("Listing azure data lake analytics accounts...")

        adla_acounts = self._adla_service.retrieve_accounts()

        self._present("(%d) azure data lake analytics account(s) listed." % (len(adla_acounts)))
        
        return self._convert_result(adla_acounts)