from typing import List
from random import randint
import re


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


class Game:
    def __init__(self, attempts, word_manager):
        self.__attempts = attempts
        self.__word_manager = word_manager
        self.__secret_word = self.__word_manager.get_secret_word()
        self.__RED = "\033[31m"
        self.__GREEN = "\033[32m"
        self.__RESET = "\033[0m"

    def start(self):
        print("Welcome to the game, are you ready to play?")
        print(f"You have {self.__attempts} attempts to guess the secret word.")
        print("Here are the words:")
        self.__word_manager.display_all_words()
        print("\033[0m" + "Let's start!")
 

    def play(self):
        attempts_left = self.__attempts
        while attempts_left > 0:
            guessed_word = input("Enter your guess: ").strip().lower()
            if not re.match("^[a-zA-Z]+$", guessed_word):
                print("Please enter English letters only.")
                continue
            if not self.__word_manager.is_word_exist(guessed_word):
                print("Please enter only words from the list")
                continue
            if guessed_word == self.__secret_word:
                print(f"{self.__GREEN}Congratulations! You've guessed the secret word correctly.{self.__RESET}")
                break
            else:
                attempts_left -= 1
                if attempts_left > 0:
                    print(f"Wrong guess! {attempts_left} attempts left.")
                else:
                    print(f"{self.__RED}Out of attempts! Game over.")
        else:
            print(f"{self.__RED}Out of attempts! You lost!{self.__RESET}")


if __name__ == "__main__":
    word_manager_factory = WordManagerFactory()
    word_manager = word_manager_factory.create_word_manager("words.txt")
    
    game = Game(3, word_manager)
    game.start()
    game.play()
    