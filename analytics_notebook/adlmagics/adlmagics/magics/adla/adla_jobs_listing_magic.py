from IPython.core.magic_arguments import magic_arguments, argument, parse_argstring
from os import linesep

from magics.adla.adla_magic_base import AdlaMagicBase

class AdlaJobsListingMagic(AdlaMagicBase):
    def __init__(self, adla_service):
        super(AdlaJobsListingMagic, self).__init__("listjobs", adla_service)

    @magic_arguments()
    @argument("--account", type = str, help = "Azure data lake account name.")
    @argument("--my", default = False, action = "store_true", help = "Only list jobs of logged in user.")
    @argument("--page_index", type = int, default = 0, help = "Paging index, starting from 0, default value: 0.")
    @argument("--page_job_number", type = int, default = 5, help = "Number of jobs per page, default value: 5.")
    def execute(self, arg_string, content_string = None):
        args = parse_argstring(self.execute, arg_string)

        job_filter = None
        if (args.my):
            job_filter = "submitter eq '%s'" % (self._adla_service.logged_in_user)

        self._write_line("Listing azure data lake jobs under account '%s'..." % (args.account))

        jobs = self._adla_service.retrieve_jobs(args.account, job_filter, args.page_index, args.page_job_number)

        html = "<table>"
        html += "    <caption>%d datalake analytics job(s) listed</caption>" % (len(jobs))
        html += "    <thead>"
        html += "        <tr>"
        html += "            <th>Job Name</th>"
        html += "            <th>Submitter</th>"
        html += "            <th>State</th>"
        html += "            <th>Result</th>"
        html += "            <th></th>"
        html += "        </tr>"
        html += "    </thead>"
        html += "    <tbody>"
        for job in jobs:
            job_details = "Parallelism: %d%s" % (job.parallelism, linesep)
            job_details += "Priority: %d%s" % (job.priority, linesep)
            job_details += "Submit Time: %s%s" % (str(job.submit_time), linesep)
            job_details += "Start Time: %s%s" % (str(job.start_time), linesep)
            job_details += "End Time: %s%s" % (str(job.end_time), linesep)
            html += "        <tr title='%s'>" % (job_details)
            html += "            <td>%s</td>" % (job.name)
            html += "            <td>%s</td>" % (job.submitter)
            html += "            <td>%s</td>" % (job.state)
            html += "            <td>%s</td>" % (job.result)
            html += "            <td><a href='https://%s.azuredatalakeanalytics.net/jobLink/%s' target='_blank'>View Job</a></td>" % (args.account, job.id)
            html += "        </tr>"
        html += "    </tbody>"
        html += "</table>"
        
        self._write_html(html)

        return self._convert_to_df(jobs)
