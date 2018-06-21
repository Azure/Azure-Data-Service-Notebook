from IPython.core.magic_arguments import magic_arguments, argument, parse_argstring

from adlmagics.magics.adls.adls_magic_base import AdlsMagicBase

class AdlsAccountsListingMagic(AdlsMagicBase):
    def __init__(self, adls_service):
        super(AdlsAccountsListingMagic, self).__init__("liststoreaccounts", adls_service)

    @magic_arguments()
    @argument("--page_index", type = int, default = 0, help = "Paging index, starting from 0, default value: 0.")
    @argument("--page_account_number", type = int, default = 5, help = "Number of accounts per page, default value: 5.")
    def execute(self, arg_string, content_string):
        args = parse_argstring(self.execute, arg_string)

        self._write_line("Listing azure data lake store accounts...")
        if args.page_index < 0:
            self._write_line("0 azure data lake store account(s) listed, because of the page_index is a negative number (we do not process it)!")
            return []

        adls_acounts = self._adls_service.retrieve_accounts(page_index = args.page_index, page_account_number = args.page_account_number)

        self._write_line("(%d) azure data lake store account(s) listed." % (len(adls_acounts)))
        
        for account in adls_acounts:
            self._write_line("%s" % (account.name))

        return self._convert_to_df(adls_acounts)