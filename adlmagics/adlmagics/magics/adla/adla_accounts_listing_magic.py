from IPython.core.magic_arguments import magic_arguments, argument, parse_argstring

from adlmagics.magics.adla.adla_magic_base import AdlaMagicBase

class AdlaAccountsListingMagic(AdlaMagicBase):
    def __init__(self, adla_service):
        super(AdlaAccountsListingMagic, self).__init__("listaccounts", adla_service)

    @magic_arguments()
    @argument("--page_index", type = int, default = 0, help = "Paging index, starting from 0, default value: 0.")
    @argument("--page_account_number", type = int, default = 5, help = "Number of accounts per page, default value: 5.")
    def execute(self, arg_string, content_string):
        args = parse_argstring(self.execute, arg_string)

        self._write_line("Listing azure data lake analytics accounts...")

        adla_acounts = self._adla_service.retrieve_accounts(page_index = args.page_index, page_account_number = args.page_account_number)

        self._write_line("(%d) azure data lake analytics account(s) listed." % (len(adla_acounts)))
        
        for account in adla_acounts:
            self._write_line("%s" % (account.name))

        return self._convert_to_df(adla_acounts)