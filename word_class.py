class Word:
    __word: str
    __color: str
    
    def __init__(self, word: str, color: str):
        self.__word = word
        self.__color = "\033[33m"    

    @property
    def word(self):
        return self.__color + self.__word
    
    @property
    def simple_word(self):
        return self.__word
    