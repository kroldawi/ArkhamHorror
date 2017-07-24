from unittest import TestCase
from game import Game

class TestGame(TestCase):
    def test_turns_passed(self):
        game = Game()
        expected = 10

        game.turns_passed = expected

        self.assertEqual(game.turns_passed, expected)

    def test_is_game_over(self):
        self.fail()
