from IPython.core.magic_arguments import magic_arguments, argument, parse_argstring

from adlmagics.magics.adls.adls_magic_base import AdlsMagicBase

class AdlsFoldersListingMagic(AdlsMagicBase):
    def __init__(self, adls_service):
        super(AdlsFoldersListingMagic, self).__init__("liststorefolders", adls_service)

    @magic_arguments()
    @argument("--account", type = str, help = "Azure data lake store account name.")
    @argument("--folder_path", default = "", help = "Relative path of the folder whose folders are to be listed.")
    def execute(self, arg_string, content_string = None):
        args = parse_argstring(self.execute, arg_string)

        self._write_line("Listing azure data lake store folders under folder '%s' of account '%s'..." % (args.folder_path, args.account))

        folders = self._adls_service.retrieve_folders(args.account, args.folder_path)

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

        self._write_html(html)

        return self._convert_to_df(folders)