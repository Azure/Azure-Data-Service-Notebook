from magics.magic_base import MagicBase

class AdlsMagicBase(MagicBase):
    def __init__(self, cmd_name, adls_service):
        super(AdlsMagicBase, self).__init__(cmd_name)

        self._adls_service = adls_service