from IPython.core.magic_arguments import magic_arguments, argument, parse_argstring

from adlmagics.magics.adla.adla_magic_base import AdlaMagicBase
from adlmagics.models.adla_job_submission import AdlaJobSubmission
from adlmagics.session_consts import session_adla_account, session_job_parallelism, session_job_priority, session_job_runtime
from adlmagics.exceptions import MagicArgumentMissingError, MagicArgumentError

class AdlaJobSubmissionMagic(AdlaMagicBase):
    def __init__(self, session_service, presenter_factory, result_converter, adla_service):
        super(AdlaJobSubmissionMagic, self).__init__("submitjob", session_service, presenter_factory, result_converter, adla_service)

    @magic_arguments()
    @argument("--account", type = str, help = "Azure data lake account name.")
    @argument("--name", type = str, help = "Azure data lake job name.")
    @argument("--parallelism", type = int, help = "Azure data lake job parallelism.")
    @argument("--priority", type = int, help = "Azure data lake job priority.")
    @argument("--runtime", type = str, help = "Azure data lake job runtime.")
    def execute(self, arg_string, content_string):
        args = parse_argstring(self.execute, arg_string)

        self.__validate_args(args)

        job_submission = AdlaJobSubmission(args.name, content_string, args.parallelism, args.priority, args.runtime)

        self._present("Submitting azure data lake job to account '%s'..." % (args.account))

        job = self._adla_service.submit_job(args.account, job_submission)

        self._present("Job submitted.")
        self._present(job)

        return self._convert_result(job)

    def __validate_args(self, args):
        self._validate_arg(args, "account", session_adla_account.name)

        if not args.name:
            raise MagicArgumentMissingError("name")

        self._validate_arg(args, "parallelism", session_job_parallelism.name)

        self._validate_arg(args, "priority", session_job_priority.name)
        # By default, the parameter `priority` is 1000 if we not set it, and the ADLA `JobInformation` class indicate that the value 
        # of `priority` should be greater than 0, but not give the limit for maximum, because Lower numbers have a higher priority,
        #  we default limit the value of priority in range [1, 1000]
        if not args.priority in range(1, 1001):
            raise MagicArgumentError("Argument 'priority' should be in range [1 - 1000] !")

        self._validate_arg(args, "runtime", session_job_runtime.name)