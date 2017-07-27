from unittest import TestCase
from player import Player


class TestPlayer(TestCase):

    def test_constructor(self):
        expected = "Player name"

        player = Player(expected)
        self.assertEqual(expected, player.name, "Player name should be set in constructor.")
        self.assertFalse(player.has_first_player_token(), "By default player shouldn't have first player token.")

        player = Player("expected", False)
        self.assertFalse(player.has_first_player_token(),
                         "First player token possession was set to false in constructor.")

        player = Player("expected", True)
        self.assertTrue(player.has_first_player_token(),
                        "First player token possession was set to true in constructor.")

    def test_name(self):
        expected = "Player name"
        player = Player(expected)

        self.assertEqual(player.name, expected)

        player.name = "Other name"
        self.assertEqual(player.name, expected)

    def test_pass_first_player_token(self):
        player = Player("New player", True)

        self.assertTrue(player.has_first_player_token(), "We wanted player to have first player token.")

        player.pass_first_player_token()
        self.assertFalse(player.has_first_player_token(),
                         "Player did have first player token so he can pass; now it shouldn't have it.")

        player.pass_first_player_token()
        self.assertFalse(player.has_first_player_token(),
                         "Player didn't have first player token so he can pass "
                         "it as much as he want and still won't have it")

    def test_receive_first_player_token(self):
        player = Player("New player", False)

        self.assertFalse(player.has_first_player_token(), "We wanted player to not have first player token.")

        player.receive_first_player_token()
        self.assertTrue(player.has_first_player_token(),
                        "Player just received first player token; he should have it then.")
