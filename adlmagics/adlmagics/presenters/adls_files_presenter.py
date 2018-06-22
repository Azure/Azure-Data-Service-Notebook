from IPython.core.display import display, HTML

from adlmagics.interfaces.presenter_base import PresenterBase
from adlmagics.models.adls_file import AdlsFile

class AdlsFilesPresenter(PresenterBase):
    def __init__(self):
        super(AdlsFilesPresenter, self).__init__(AdlsFilesPresenter)

    def present(self, obj):
        if (not obj) or (not obj is list):
            return

        files = obj as list

        if not all(isinstance(f, AdlsFile) for f in files):
            return

        html = "<table>"
        html += "    <caption>%d datalake store file(s) listed</caption>" % (len(files))
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
        for f in files:
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