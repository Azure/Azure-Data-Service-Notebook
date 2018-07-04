from adlmagics.session_consts import *

class MockSessionService:
    def __init__(self, persister):
        self.__persister = persister

        self.__session_items = {
            session_tenant.name : session_tenant.default_value,
            session_user.name : session_user.default_value,

            session_adla_account.name : session_adla_account.default_value,

            session_adls_account.name : session_adls_account.default_value,

            session_job_runtime.name : session_job_runtime.default_value,
            session_job_priority.name : session_job_priority.default_value,
            session_job_parallelism.name : session_job_parallelism.default_value,

            session_paging_numberperpage.name : session_paging_numberperpage.default_value,

            session_file_encoding.name : session_file_encoding.default_value
        }

        self.__session_item_names = [*self.__session_items]

        self.__load()

    def set_session_item(self, name, value):
        if not name:
            return

        if not self.contains_session_item(name):
            return

        self.__session_items[name] = value

        self.__persist()

    def get_session_item(self, name):
        if not name:
            return session_null_value

        if not self.contains_session_item(name):
            return session_null_value

        return self.__session_items[name]

    def contains_session_item(self, name):
        if not name:
            return False

        return name in self.__session_item_names

    @property
    def session_item_names(self):
        return self.__session_item_names

    def __load(self):
        tmp_dict = self.__persister.load()
        if tmp_dict:
            self.__session_items.update(tmp_dict)
    
    def __persist(self):
        self.__persister.save(self.__session_items)