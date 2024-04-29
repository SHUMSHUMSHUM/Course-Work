from test import WordManagerFactory
from test import Game

if __name__ == "__main__":
    word_manager_factory = WordManagerFactory()
    word_manager = word_manager_factory.create_word_manager("words.txt")
    
    game = Game(3, word_manager)
    game.start()
    game.play()