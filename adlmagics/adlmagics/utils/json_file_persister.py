from json import load, dump
from pathlib import Path

class JsonFilePersister:
    def __init__(self, file_full_path, file_encoding):
        self.__file_full_path = Path(file_full_path)
        self.__file_encoding = file_encoding

    def load(self):
        if not self.__file_full_path.exists():
            return dict()
        
        with self.__file_full_path.open("r", encoding = self.__file_encoding) as f:
            return load(f)

    def save(self, obj):
        with self.__file_full_path.open("w+", encoding = self.__file_encoding) as f:
            dump(obj, f, ensure_ascii = False)


    