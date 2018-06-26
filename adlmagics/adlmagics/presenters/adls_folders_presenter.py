from IPython.core.display import display, HTML

from adlmagics.presenters.presenter_base import PresenterBase
from adlmagics.models.adls_folder import AdlsFolder

class AdlsFoldersPresenter(PresenterBase):
    def is_presentable(self, obj):
        return (obj is list) and all(isinstance(f, AdlsFolder) for f in obj)

    def present(self, obj):
        super(AdlsFoldersPresenter, self).present(obj)

        html = "<table>"
        html += "    <caption>%d datalake store folder(s) listed</caption>" % (len(obj))
        html += "    <thead>"
        html += "        <tr>"
        html += "            <th>Folder Name</th>"
        html += "            <th>Last Access Time</th>"
        html += "            <th>Last Modified Time</th>"
        html += "            <th>Path</th>"
        html += "        </tr>"
        html += "    </thead>"
        html += "    <tbody>"
        for folder in obj:
            html += "        <tr>"
            html += "            <td>%s</td>" % (folder.name)
            html += "            <td>%s</td>" % (str(folder.last_access_time))
            html += "            <td>%s</td>" % (str(folder.last_modified_time))
            html += "            <td>%s</td>" % (folder.path)
            html += "        </tr>"
        html += "    </tbody>"
        html += "</table>"

        display(HTML(html))