from adlmagics.magics.session.session_magic_base import SessionMagicBase

class SessionListingMagic(SessionMagicBase):
    def __init__(self, cmd_name):
        super(SessionListingMagic, self).__init__(cmd_name)
        
    def execute(self, arg_string, content_string = None):