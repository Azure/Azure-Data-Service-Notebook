from IPython.core.magic_arguments import magic_arguments, argument, parse_argstring

from adlmagics.magics.adla.adla_magic_base import AdlaMagicBase
from adlmagics.session_consts import session_adla_account
from adlmagics.exceptions import MagicArgumentMissingError

class AdlaJobViewingMagic(AdlaMagicBase):
    def __init__(self, session_service, presenter_factory, result_converter, adla_service):
        super(AdlaJobViewingMagic, self).__init__("viewjob", session_service, presenter_factory, result_converter, adla_service)

    @magic_arguments()
    @argument("--account", type = str, help = "Azure data lake account name.")
    @argument("--job_id", type = str, help = "Azure data lake job id.")
    def execute(self, arg_string, content_string):
        args = parse_argstring(self.execute, arg_string)

        self.__validate_args(args)

        self._present("Viewing azure data lake job by id '%s' under account '%s'..." % (args.job_id, args.account))

        job = self._adla_service.retrieve_job(args.account, args.job_id)

        self._present(job)

        return self._convert_result(job)
    
    def __validate_args(self, args):
        self._validate_arg(args, "account", session_adla_account.name)

        if not args.job_id:
            raise MagicArgumentMissingError("job_id")