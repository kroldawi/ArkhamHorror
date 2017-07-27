import unittest
from game import Game
from player import Player


PLAYERS = [Player("Joanna"), Player("Dawid", True), Player("Carrie")]


class TestGame(unittest.TestCase):

    def test_turns_cap(self):
        game = Game()

        game.turns_cap = 10
        self.assertNotEqual(game.turns_cap, 10)

    def test_turns_passed(self):
        game = Game()
        expected = 10

        game.turns_passed = expected
        self.assertEqual(game.turns_passed, expected)

        with self.assertRaises(ValueError):
            game.turns_passed = -1

    def test_is_game_over(self):
        game = Game()

        game.turns_passed = game.turns_cap - 1
        self.assertFalse(game.is_game_over())

        game.turns_passed = game.turns_cap + 1
        self.assertTrue(game.is_game_over())

if __name__ == '__main__':
    unittest.main()
