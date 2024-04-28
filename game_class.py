import re
from wordmanager_class import WordManager

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
