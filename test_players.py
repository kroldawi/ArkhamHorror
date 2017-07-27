import unittest
from players import Players
from player import Player

PLAYERS_CORRECT = [Player("Joanna"), Player("Dawid", True), Player("Carrie")]
PLAYERS_INCORRECT = [Player("Joanna"), Player("Dawid", False), Player("Carrie")]


class TestPlayers(unittest.TestCase):

    def test_players(self):
        players = Players(PLAYERS_CORRECT)
        self.assertTrue(players.players, PLAYERS_CORRECT)

        players.players = None
        self.assertEqual(players.players, PLAYERS_CORRECT)

    def test_constructor(self):
        players = Players()
        self.assertEqual(len(players.players), 1, "By default we should have one player.")

    def test_first_player(self):
        players = Players()
        self.assertEqual(players.first_player(), players.players[0],
                         "By default first player in collection should be the first player in a game.")

        players = Players(PLAYERS_CORRECT)
        self.assertEqual(players.first_player(), PLAYERS_CORRECT[1],
                         "In set of players we passed to Game constructor second plaYer has first player token.")

        players = Players(PLAYERS_INCORRECT)
        with self.assertRaises(ValueError):
            players.first_player()

    def test_next_player(self):
        players = Players(PLAYERS_CORRECT)

        self.assertEqual(len(players.players), 3, "Double checking that we have exactly 3 players.")
        self.assertEqual(players.next_player(1), 2, "Player 2 goes after player 1")
        self.assertEqual(players.next_player(2), 0, "Player 0 goes after player 2")
        self.assertEqual(players.next_player(0), 1, "Player 1 goes after player 0")

    def test_pass_first_player_token(self):
        players = Players(PLAYERS_CORRECT)

        self.assertTrue(not players.players[0].has_first_player_token()
                        and players.players[1].has_first_player_token()
                        and not players.players[2].has_first_player_token(),
                        "In set of players we passed to Game constructor second player has first player token.")

        players.pass_first_player_token()
        self.assertTrue(not players.players[0].has_first_player_token()
                        and not players.players[1].has_first_player_token()
                        and players.players[2].has_first_player_token(),
                        "We have passed first player token so third player has first player token.")

        players.pass_first_player_token()
        self.assertEqual(players.first_player(), PLAYERS_CORRECT[0],
                         "We have three players, so new current player should be 0th - we move in a loop.")

if __name__ == '__main__':
    unittest.main()
