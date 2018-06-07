class AdlsFolder:
    def __init__(self, name, path, last_access_time, last_modified_time):
        self.name = name
        self.path = path
        self.last_access_time = last_access_time
        self.last_modified_time = last_modified_time