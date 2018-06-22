from IPython.core.magic_arguments import magic_arguments, argument, parse_argstring
from pathlib import Path

from adlmagics.magics.adls.adls_magic_base import AdlsMagicBase
from adlmagics.session_consts import session_adls_account, session_file_encoding
from adlmagics.exceptions import MagicArgumentMissingError, MagicArgumentError

class AdlsFileSamplingMagic(AdlsMagicBase):
    def __init__(self, session_service, presenter_factory, result_converter, adls_service):
        super(AdlsFileSamplingMagic, self).__init__("sample", session_service, presenter_factory, result_converter, adls_service)

        self.__fileTypeColumnSepMappings = { "tsv" : "\t", "csv" : ",", "txt" : None }

    @magic_arguments()
    @argument("--account", type = str, help = "Azure data lake store account name.")
    @argument("--file_path", type = str, help = "Path of the file to be sampled.")
    @argument("--file_type", choices = ["tsv", "csv", "txt"], help = "Type of the file. Supported value: tsv, csv or txt.")
    @argument("--encoding", default = "utf-8", help = "Encoding of the file. Default is 'utf-8'")
    @argument("--row_number", type = int, default = 50, help = "Number of rows to be read from the file. Default is 50.")
    def execute(self, arg_string, content_string):
        args = parse_argstring(self.execute, arg_string)

        self.__validate_args(args)

        self._present("Sampling data lake store file '%s'..." % (args.file_path))

        read_lines = self._adls_service.read_file(args.account, args.file_path, args.encoding, self.__fileTypeColumnSepMappings[args.file_type], args.row_number)

        self._present("(%d) row(s) sampled." % (len(read_lines)))
        
        return self._convert_result(read_lines)

    def __validate_args(self, args):
        self._validate_arg(args, "account", session_adls_account.name)

        if not args.file_path:
            raise MagicArgumentMissingError("file_path")

        if not args.file_type:
            file_ext = Path(args.file_path).suffix
            if not file_ext:
                raise MagicArgumentMissingError("file_type")
            else:
                args.file_type = file_ext[1:]

        self._validate_arg(args, "encoding", session_file_encoding.name)

        if args.row_number <= 0:
            raise MagicArgumentError("Argument 'row_number' should be greater than 0.")