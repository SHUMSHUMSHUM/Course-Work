from word import Word
from random import randint
from typing import List


class WordManager:
    def __init__(self, word_list: List[str]):
        self.__words = []
        indices = set()
        while len(indices) < 5:
            index = randint(0, len(word_list) - 1)
            if index not in indices:
                indices.add(index)
                self.__words.append(Word(word_list[index], "\033[33m"))
                
    def display_all_words(self):
        for word in self.__words:
            print(word.formatted_word)

    def get_secret_word(self):
        return self.__words[randint(0, len(self.__words) - 1)].simple_word

    def is_word_exist(self, guessed_word):
        return any(word.simple_word == guessed_word for word in self.__words)

