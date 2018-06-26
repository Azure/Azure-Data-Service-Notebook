from adlmagics.magics.magic_base import MagicBase

class AzureMagicBase(MagicBase):
    def __init__(self, cmd_name, session_service, presenter_factory, token_service):
        super(AzureMagicBase, self).__init__(cmd_name, session_service, presenter_factory)

        self._token_service = token_service