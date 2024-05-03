import unittest
from unittest.mock import patch
from game import Game
from wordmanager_factory import WordManagerFactory


class TestGame(unittest.TestCase):
    def setUp(self):
        word_manager_factory = WordManagerFactory()
        word_manager = word_manager_factory.create_word_manager("test_words.txt")
        self.game = Game(3, word_manager)

    def test_guess_secret_word_correctly(self):
        self.assertEqual(self.game.play("test_word"), "\033[32mCongratulations! You've guessed the secret word correctly.\033[0m")

    def test_out_of_attempts_lost(self):
        self.assertEqual(self.game.play("wrong_word"), "\033[31mOut of attempts! You lost!\033[0m")

    def test_invalid_guess(self):
        self.assertEqual(self.game.play("!@#"), "Please enter English letters only.")

    def test_wrong_guess(self):
        self.assertEqual(self.game.play("wrong_word"), "Wrong guess! 2 attempts left.")

    def test_word_display(self):
        self.assertEqual(self.game.start(), None)


if __name__ == '__main__':
    unittest.main()
