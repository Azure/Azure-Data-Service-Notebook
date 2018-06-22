from adlmagics.magics.magic_base import MagicBase

class SessionMagicBase(MagicBase):
    def __init__(self, cmd_name, session_service, presenter_factory, result_converter):
        super(SessionMagicBase, self).__init__(cmd_name, session_service, presenter_factory, result_converter)