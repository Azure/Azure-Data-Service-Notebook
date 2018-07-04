from sys import stdout
from os import linesep

from adlmagics.presenters.presenter_base import PresenterBase
from adlmagics.models.adla_job import AdlaJob

class AdlaJobPresenter(PresenterBase):
    def is_presentable(self, obj):
        return isinstance(obj, AdlaJob)

    def present(self, obj):
        super(AdlaJobPresenter, self).present(obj)

        self.__write_line("Job info:")
        self.__write_line("  Id: %s" % (obj.id))
        self.__write_line("  Name: %s" % (obj.name))
        self.__write_line("  Type: %s" % (obj.type))
        self.__write_line("  Submitter: %s" % (obj.submitter))
        self.__write_line("  Parallelism: %d" % (obj.parallelism))
        self.__write_line("  Priority: %d" % (obj.priority))
        self.__write_line("  Submit time: %s" % (str(obj.submit_time)))
        self.__write_line("  Start time: %s" % (str(obj.start_time)))
        self.__write_line("  End time: %s" % (str(obj.end_time)))
        self.__write_line("  State: %s" % (obj.state))
        self.__write_line("  Result: %s" % (obj.result))

    def __write_line(self, text):
        stdout.write(text + linesep)