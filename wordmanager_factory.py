from wordmanager import WordManager
from filereader import FileReader


class WordManagerFactory:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def create_word_manager(self, file_path: str) -> 'WordManager':
        file_reader = FileReader(file_path)
        file_reader.read()
        word_list = file_reader.data.split("\n")
        return WordManager(word_list)
    #using factroy and singelton
