from IPython.core.display import display, HTML

from adlmagics.interfaces.presenter_base import PresenterBase
from adlmagics.models.adls_folder import AdlsFolder

class AdlsFoldersPresenter(PresenterBase):
    def __init__(self):
        super(AdlsFoldersPresenter, self).__init__(AdlsFoldersPresenter)

    def present(self, obj):
        if (not obj) or (not obj is list):
            return

        folders = obj as list

        if not all(isinstance(f, AdlsFolder) for f in folders):
            return

        html = "<table>"
        html += "    <caption>%d datalake store folder(s) listed</caption>" % (len(folders))
        html += "    <thead>"
        html += "        <tr>"
        html += "            <th>Folder Name</th>"
        html += "            <th>Last Access Time</th>"
        html += "            <th>Last Modified Time</th>"
        html += "            <th>Path</th>"
        html += "        </tr>"
        html += "    </thead>"
        html += "    <tbody>"
        for f in folders:
            html += "        <tr>"
            html += "            <td>%s</td>" % (f.name)
            html += "            <td>%s</td>" % (str(f.last_access_time))
            html += "            <td>%s</td>" % (str(f.last_modified_time))
            html += "            <td>%s</td>" % (f.path)
            html += "        </tr>"
        html += "    </tbody>"
        html += "</table>"

        display(HTML(html))