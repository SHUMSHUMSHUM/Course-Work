class FileReader:
    def __init__(self, path: str):
        self.__path = path
        self.__data = ""

    def read(self):
        with open(self.__path, "r") as f:
            self.__data = f.read()

    @property
    def data(self):
        return self.__data