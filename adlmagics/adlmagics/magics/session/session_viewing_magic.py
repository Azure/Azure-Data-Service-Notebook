from adlmagics.magics.session.session_magic_base import SessionMagicBase

class SessionViewingMagic(SessionMagicBase):
    def __init__(self, session_service, presenter_factory):
        super(SessionListingMagic, self).__init__("viewsession", session_service, presenter_factory)
        
    def execute(self, arg_string, content_string):
        self._present("Session items:")

        for session_item_name in self._session_service.session_item_names:
            self._present("  %s : %s" % (session_item_name, self._session_service.get_session_item(session_item_name)))
        