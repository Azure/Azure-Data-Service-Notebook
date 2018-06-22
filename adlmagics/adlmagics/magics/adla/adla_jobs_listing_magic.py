from IPython.core.magic_arguments import magic_arguments, argument, parse_argstring
from os import linesep

from adlmagics.magics.adla.adla_magic_base import AdlaMagicBase
from adlmagics.session_consts import session_adla_account, session_paging_numberperpage
from adlmagics.exceptions import MagicArgumentError

class AdlaJobsListingMagic(AdlaMagicBase):
    def __init__(self, session_service, presenter_factory, result_converter, adla_service):
        super(AdlaJobsListingMagic, self).__init__("listjobs", session_service, presenter_factory, result_converter, adla_service)

    @magic_arguments()
    @argument("--account", type = str, help = "Azure data lake account name.")
    @argument("--my", default = False, action = "store_true", help = "Only list jobs of logged in user.")
    @argument("--page_index", type = int, default = 0, help = "Paging index, starting from 0, default value: 0.")
    @argument("--page_job_number", type = int, default = 5, help = "Number of jobs per page, default value: 5.")
    def execute(self, arg_string, content_string):
        args = parse_argstring(self.execute, arg_string)

        self.__validate_args(args)

        job_filter = None
        if (args.my):
            job_filter = "submitter eq '%s'" % (self._adla_service.logged_in_user)

        self._present("Listing azure data lake jobs under account '%s'..." % (args.account))

        jobs = self._adla_service.retrieve_jobs(args.account, job_filter, args.page_index, args.page_job_number)

        self._present("(%d) azure data lake job(s) listed." % (len(jobs)))
        self._present(jobs)

        return self._convert_result(jobs)

    def __validate_args(self, args):
        self._validate_arg(args, "account", session_adla_account.name)

        if args.page_index < 0:
            raise MagicArgumentError("Argument 'page_index' must be greater than or equal to 0")

        self._validate_arg(args, "page_job_number", session_paging_numberperpage.name)
        if args.page_job_number <= 0:
            raise MagicArgumentError("Argument 'page_job_number' must be greater than 0")