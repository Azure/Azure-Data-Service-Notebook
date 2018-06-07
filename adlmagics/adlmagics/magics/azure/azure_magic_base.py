from adlmagics.magics.magic_base import MagicBase

class AzureMagicBase(MagicBase):
    def __init__(self, cmd_name, token_service):
        super(AzureMagicBase, self).__init__(cmd_name)

        self._token_service = token_service