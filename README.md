
### 1. Introduction

#### Application Description:

The application is a word guessing game implemented in Python. It allows users to guess a secret word chosen from a predefined list within a limited number of attempts. It can be easily modified to increase the number of attempts or words that are provided to the list.

#### How to Run the Program:

To run the program, ensure you have Python installed on your system. Save the provided code in a file named word_game.py. Additionally, install a file named words.txt containing a list of words separated by newline characters. Combine those files in one folder. Then, open any IDE and open that folder. Execute the program by running python word_game.py in the terminal.

#### How to Use the Program:

Once the program is running, follow the prompts on the terminal. You'll be presented with a list of words from which you need to guess the secret word. Enter your guesses, and the program will provide feedback on whether your guess is correct or not. You have a limited number of attempts to guess the word, 3 by default, can be modified.

### 2. Body/Analysis

#### Functional Requirements Implementation:

The program fulfills the following functional requirements:

-   Display Words: Displays a list of words from which the player needs to guess.
    
-   Guess Secret Word: Allows the player to input guesses until they either guess the secret word correctly or run out of attempts.
    
-   Validation: Ensures the input is a valid English word from the provided list and provides appropriate feedback.
    
-   Reads words from the file.
    
-   Utilizes singleton and builder design patterns
    

### 3. Results and Summary

-   Results:
    

-   Implemented the word guessing game functionality.
    
-   Completed part that validates user input and ensures it matches the provided word list.
    
-   Validating misspelled words or other english words took the longest
    

#### Conclusions

The implemented program provides an engaging word guessing experience for users. It meets the specified functional requirements. Future prospects include:

-   Adding more features such as difficulty levels.
    
-   Implementing a graphical user interface (GUI) for enhanced user experience.
    
-   Incorporating a scoring system to track player performance over multiple rounds.

#### References

-  https://peps.python.org/pep-0008/

-  https://www.markdownguide.org/basic-syntax/

-  additional thanks to a friend that sugested to make such game   
