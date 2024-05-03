import re

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
