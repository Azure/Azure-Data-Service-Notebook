from adlmagics.magics.magic_base import MagicBase

class AdlsMagicBase(MagicBase):
    def __init__(self, cmd_name, session_service, presenter_factory, result_converter, adls_service):
        super(AdlsMagicBase, self).__init__(cmd_name, session_service, presenter_factory, result_converter)

        self._adls_service = adls_service