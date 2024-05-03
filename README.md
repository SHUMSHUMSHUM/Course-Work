#   Coursework Report

## 1. Introduction

###  What is your application?

The application is a word guessing game implemented in Python. It allows users to guess a secret word chosen from a predefined list within a limited number of attempts. It can be easily modified to increase the number of attempts or words that are provided to the list.

###  How to run the program?

To run the program, execute the `main.py` file in a Python environment. Make sure all necessary files are in the same directory as the program files.

###  How to use the program?

Once the program is running, follow the prompts on the terminal. You'll be presented with a list of words from which you need to guess the secret word. Enter your guesses, and the program will provide feedback on whether your guess is correct or not. You have a limited number of attempts to guess the word, 3 by default, can be modified.

## 2. Body/Analysis

###  Explain how the program covers functional requirements

The program covers the following functional requirements:

-   **Word Generation**: The `WordManager` class generates a list of words from a file and selects a secret word from this list.

-   **Word Display**: The `WordManager` class displays a subset of words from the list for the player to see.

-   **Word Guessing**: The `Game` class allows the player to input guesses and provides feedback on whether the guess is correct or not.

-   **Game Over**: The game ends when the player either guesses the word correctly or runs out of attempts.

## 3. Results and Summary

###  Results

-   The implementation of the game successfully allows players to guess words from a provided list.
-  Completed part that validates user input and ensures it matches the provided word list.
    
-   Validating misspelled words or other English words took the longest

-   Added unittesting functionality

###  Conclusions

The implementation of the word guessing game achieves the goal of providing an interactive game experience for users. 

###  Future Prospects

Future prospects of the program include:

-   Adding more features such as difficulty levels.
    
-   Implementing a graphical user interface (GUI) for enhanced user experience.
    
-   Incorporating a scoring system to track player performance over multiple rounds.


## 4. Optional: Resources, references list

-  Special thanks to a friend that suggested to make such game   

-  https://peps.python.org/pep-0008/

-  https://www.markdownguide.org/basic-syntax/

-  https://github.com/coala/coala-bears/issues/2862

- https://refactoring.guru/design-patterns/factory-method

- https://refactoring.guru/design-patterns/singleton
