from IPython.core.magic_arguments import magic_arguments, argument, parse_argstring
from pandas import DataFrame

from adlmagics.magics.adls.adls_magic_base import AdlsMagicBase

class AdlsFileSamplingMagic(AdlsMagicBase):
    def __init__(self, adls_service):
        super(AdlsFileSamplingMagic, self).__init__("sample", adls_service)

        self.__fileTypeColumnSepMappings = { "tsv" : "\t", "csv" : ",", "txt" : None }

    @magic_arguments()
    @argument("--account", type = str, help = "Azure data lake store account name.")
    @argument("--file_path", type = str, help = "Path of the file to be sampled.")
    @argument("--file_type", choices = ["tsv", "csv", "txt"], help = "Type of the file. Supported value: tsv, csv or txt.")
    @argument("--encoding", default = "utf-8", help = "Encoding of the file. Default is 'utf-8'")
    @argument("--row_number", type = int, default = 50, help = "Number of rows to be read from the file. Default is 50.")
    def execute(self, arg_string, content_string):
        args = parse_argstring(self.execute, arg_string)

        self._write_line("Sampling data lake store file '%s'..." % (args.file_path))

        read_lines = self._adls_service.read_file(args.account, args.file_path, args.encoding, self.__fileTypeColumnSepMappings[args.file_type], args.row_number)

        self._write_line("(%d) row(s) sampled." % (len(read_lines)))
        
        for read_line in read_lines:
            self._write_line("%s" % (read_line))

        return DataFrame(read_lines)