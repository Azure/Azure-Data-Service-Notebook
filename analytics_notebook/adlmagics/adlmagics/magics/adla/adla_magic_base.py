from magics.magic_base import MagicBase

class AdlaMagicBase(MagicBase):
    def __init__(self, cmd_name, adla_service):
        super(AdlaMagicBase, self).__init__(cmd_name)

        self._adla_service = adla_service