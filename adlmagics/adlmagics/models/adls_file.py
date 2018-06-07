class AdlsFile:
    def __init__(self, name, path, size_in_bytes, last_access_time, last_modified_time):
        self.name = name
        self.path = path
        self.size_in_bytes = size_in_bytes
        self.last_access_time = last_access_time
        self.last_modified_time = last_modified_time