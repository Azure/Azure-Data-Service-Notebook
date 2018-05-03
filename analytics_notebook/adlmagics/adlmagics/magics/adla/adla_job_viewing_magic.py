from IPython.core.magic_arguments import magic_arguments, argument, parse_argstring

from magics.adla.adla_magic_base import AdlaMagicBase

class AdlaJobViewingMagic(AdlaMagicBase):
    def __init__(self, adla_service):
        super(AdlaJobViewingMagic, self).__init__("viewjob", adla_service)

    @magic_arguments()
    @argument("--account", type = str, help = "Azure data lake account name.")
    @argument("--job_id", type = str, help = "Azure data lake job id.")
    def execute(self, arg_string, content_string = None):
        args = parse_argstring(self.execute, arg_string)

        self._write_line("Viewing azure data lake job by id '%s' under account '%s'..." % (args.job_id, args.account))

        job = self._adla_service.retrieve_job(args.account, args.job_id)

        self._write_line("Azure data lake job info:")
        self._write_line("\tName: %s" % (job.name))
        self._write_line("\tType: %s" % (job.type))
        self._write_line("\tSubmitter: %s" % (job.submitter))
        self._write_line("\tParallelism: %d" % (job.parallelism))
        self._write_line("\tPriority: %d" % (job.priority))
        self._write_line("\tSubmit time: %s" % (str(job.submit_time)))
        self._write_line("\tStart time: %s" % (str(job.start_time)))
        self._write_line("\tEnd time: %s" % (str(job.end_time)))
        self._write_line("\tState: %s" % (job.state))
        self._write_line("\tResult: %s" % (job.result))

        return self._convert_to_df([job])