from typing import List
from random import randint
import re


class FileReader:
    __path: str
    __data: str
    
    def __init__(self, path: str):
        self.__path = path
    
    def read(self):
        with open(self.__path, "r") as f:
            self.__data = f.read()
    
    @property
    def data(self):
        return self.__data


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

class Game:
    __attempts: int
    
    def __init__(self, attempts):
        self.__attempts = attempts
        self.__word_manager = WordManager()
        self.__secret_word = self.__word_manager.secret_word()

    def start(self):
        print("Welcome to the game, are you ready to play?")
        print(f"You have {self.__attempts} attempts to guess the secret word.")
        print("Here are the words:")
        self.__word_manager.display_all_words()
        print("\033[0m" + "Let's starts! ")

    def play(self):
        attempts_left = self.__attempts
        while attempts_left > 0:
            guessed_word = input("Enter your guess: ").strip().lower()
            if not re.match("^[a-zA-Z]+$", guessed_word):
                print("Please enter english letters only only.")
                continue
            if  not self.__word_manager.is_word_exist (guessed_word):
                print("Please enter only words from the list")
                continue             
            if guessed_word == self.__secret_word:
                print("Congratulations! You've guessed the secret word correctly.")
                break
            else:
                attempts_left -= 1
                if attempts_left > 0:
                    print(f"Wrong guess! {attempts_left} attempts left.")
                else:
                    print("Out of attempts! Game over.")
        else:
            print("Out of attempts! You lost!")

if __name__ == "__main__":
    game = Game(3)
    game.start()
    game.play()
    