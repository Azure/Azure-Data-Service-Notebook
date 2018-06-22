from sys import stdout
from os import linesep

from adlmagics.interfaces.presenter_base import PresenterBase
from adlmagics.models.adla_job import AdlaJob

class AdlaJobPresenter(PresenterBase):
    def __init__(self):
        super(AdlaJobPresenter, self).__init__(AdlaJob)

    def present(self, obj):
        if (not obj) or (not obj is AdlaJob):
            return

        job = obj as AdlaJob

        self.__write_line("Job info:")
        self.__write_line("  Id: %s" % (job.id))
        self.__write_line("  Name: %s" % (job.name))
        self.__write_line("  Type: %s" % (job.type))
        self.__write_line("  Submitter: %s" % (job.submitter))
        self.__write_line("  Parallelism: %d" % (job.parallelism))
        self.__write_line("  Priority: %d" % (job.priority))
        self.__write_line("  Submit time: %s" % (str(job.submit_time)))
        self.__write_line("  Start time: %s" % (str(job.start_time)))
        self.__write_line("  End time: %s" % (str(job.end_time)))
        self.__write_line("  State: %s" % (job.state))
        self.__write_line("  Result: %s" % (job.result))

    def __write_line(self, text):
        stdout.write(text + linesep)