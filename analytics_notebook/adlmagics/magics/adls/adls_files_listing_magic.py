from IPython.core.magic_arguments import magic_arguments, argument, parse_argstring

from magics.adls.adls_magic_base import AdlsMagicBase

class AdlsFilesListingMagic(AdlsMagicBase):
    def __init__(self, adls_service):
        super(AdlsFilesListingMagic, self).__init__("liststorefiles", adls_service)

    @magic_arguments()
    @argument("--account", type = str, help = "Azure data lake store account name.")
    @argument("--folder_path", default = "", help = "Relative path of the folder whose files are to be listed.")
    def execute(self, arg_string, content_string = None):
        args = parse_argstring(self.execute, arg_string)

        self._write_line("Listing azure data lake store files under folder '%s' of account '%s'..." % (args.folder_path, args.account))

        files = self._adls_service.retrieve_files(args.account, args.folder_path)

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

        self._write_html(html)

        return self._convert_to_df(files)