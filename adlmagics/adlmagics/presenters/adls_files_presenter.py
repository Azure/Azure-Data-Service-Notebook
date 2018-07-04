from IPython.core.display import display, HTML

from adlmagics.presenters.presenter_base import PresenterBase
from adlmagics.models.adls_file import AdlsFile

class AdlsFilesPresenter(PresenterBase):
    def is_presentable(self, obj):
        return isinstance(obj, list) and all(isinstance(f, AdlsFile) for f in obj)

    def present(self, obj):
        super(AdlsFilesPresenter, self).present(obj)

        html = "<table>"
        html += "    <caption>%d datalake store file(s) listed</caption>" % (len(obj))
        html += "    <thead>"
        html += "        <tr>"
        html += "            <th>File Name</th>"
        html += "            <th>Size (Bytes)</th>"
        html += "            <th>Last Access Time</th>"
        html += "            <th>Last Modified Time</th>"
        html += "            <th>Path</th>"
        html += "        </tr>"
        html += "    </thead>"
        html += "    <tbody>"
        for f in obj:
            html += "        <tr>"
            html += "            <td>%s</td>" % (f.name)
            html += "            <td>%s</td>" % (f.size_in_bytes)
            html += "            <td>%s</td>" % (str(f.last_access_time))
            html += "            <td>%s</td>" % (str(f.last_modified_time))
            html += "            <td>%s</td>" % (f.path)
            html += "        </tr>"
        html += "    </tbody>"
        html += "</table>"

        display(HTML(html))