class SessionManager:
    class __Singleton:
        def __init__(self):
            self.active_adla_account = None
            self.active_adls_acount = None
            self.item_number_per_page = 10
    
    __instance = None

    def __new__(cls):
        if (not SessionManager.__instance):
            SessionManager.__instance = SessionManager.__Singleton()

        return SessionManager.__instance

    @staticmethod
    def get_instance():
        return SessionManager()

    @property
    def active_adla_account(self):
        return SessionManager.__instance.active_adla_account

    @active_adla_account.setter
    def active_adla_account(self, value):
        SessionManager.__instance.active_adla_account = value

    @property
    def active_adls_account(self):
        return SessionManager.__instance.active_adls_acount

    @active_adls_account.setter
    def active_adls_account(self, value):
        SessionManager.__instance.active_adls_acount = value

    @property
    def item_number_per_page(self):
        return SessionManager.__instance.item_number_per_page

    @item_number_per_page.setter
    def item_number_per_page(self, value):
        if (value is not int):
            raise TypeError("Value should be an int.")

        if (value <= 0):
            raise ValueError("Value should be greater than 0.")

        SessionManager.__instance.item_number_per_page = value