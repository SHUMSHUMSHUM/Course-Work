from word_class import Word
from filereader_class import FileReader
from random import randint
from typing import List

class WordManager:
    __words: List[Word]
    __secret_word: Word

    def __init__(self):
        self.__words = []
        
        file_reader = FileReader("words.txt")
        file_reader.read()
        
        data = file_reader.data
        split_data = data.split("\n")
        
        for i in range(5):
            index = randint(0, len(split_data) - 1)
            word_str = split_data[index]
            
            word = Word(word_str, "\033[0m")
            self.__words.append(word)

    def display_all_words(self):
        for word in self.__words:
            print(word.word)
        
    def secret_word(self):
        secret_word = self.__words[randint(0, len(self.__words) - 1)]
        return secret_word.simple_word

    def is_word_exist(self, guessed_word):
        for word in self.__words:
            if word.simple_word == guessed_word:
                return True
        
        return False
    


    