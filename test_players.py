from unittest import TestCase
from players import Players
from player import Player

PLAYERS = [Player("Joanna"), Player("Dawid", True), Player("Carrie")]


class TestPlayers(TestCase):

    def test_players(self):
        players = Players(PLAYERS)

        self.assertTrue(players.players, PLAYERS)

        players.players = None
        self.assertEqual(players.players, PLAYERS)

    def test_first_player(self):
        players = Players()
        self.assertEqual(players.first_player(), 0,
                         "By default first player in collection should be the first player in a game.")

        players = Players(PLAYERS)
        self.assertEqual(players.first_player(), 1,
                         "In set of players we passed to Game constructor second plaYer has first player token.")

        players = Players([Player("Dawid", False)])
        with self.assertRaises(ValueError):
            players.first_player()

    def test_pass_first_player_token(self):
        players = Players(PLAYERS)
        self.assertEqual(players.first_player(), 1,
                         "In set of players we passed to Game constructor second plaYer has first player token.")

        players.pass_first_player_token()
        self.assertEqual(players.first_player(), 2,
                         "We have three players, so new current player should be 2nd.")

        players.pass_first_player_token()
        self.assertEqual(players.first_player(), 0,
                         "We have three players, so new current player should be 0th - we move in a loop.")
