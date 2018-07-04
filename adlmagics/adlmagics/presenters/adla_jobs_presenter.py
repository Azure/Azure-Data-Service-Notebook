from IPython.core.display import display, HTML
from os import linesep

from adlmagics.presenters.presenter_base import PresenterBase
from adlmagics.models.adla_job import AdlaJob

class AdlaJobsPresenter(PresenterBase):
    def is_presentable(self, obj):
        return isinstance(obj, list) and all(isinstance(job, AdlaJob) for job in obj)

    def present(self, obj):
        super(AdlaJobsPresenter, self).present(obj)

        html = "<table>"
        html += "    <caption>%d datalake analytics job(s) listed</caption>" % (len(obj))
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
        for job in obj:
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
            html += "            <td><a href='https://%s.azuredatalakeanalytics.net/jobs/%s' target='_blank'>View Job</a></td>" % (job.account, job.id)
            html += "        </tr>"
        html += "    </tbody>"
        html += "</table>"

        display(HTML(html))