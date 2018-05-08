from adlmagics.magics.magic_base import MagicBase
from adlmagics.services.session_manager import SessionManager

class SessionMagicBase(MagicBase):
    def __init__(self, cmd_name):
        super(SessionMagicBase, self).__init__(cmd_name)
        self._session_manager = SessionManager.get_instance()