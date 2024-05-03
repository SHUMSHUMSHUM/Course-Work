class Word:
    def __init__(self, word: str, color: str):
        self.__word = word
        self.__color = color

    @property
    def formatted_word(self):
        return self.__color + self.__word

    @property
    def simple_word(self):
        return self.__word
