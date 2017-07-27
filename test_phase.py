import unittest
from phase import Phase
from players import Players


class MockPlayers(Players):
    def __init__(self, all_players_played):
        self.__all_players_played = all_players_played

    def has_all_players_played(self):
        return self.__all_players_played


class TestPhase(unittest.TestCase):

    def test_name(self):
        expected = "Phase name"
        phase = Phase(expected)

        self.assertEqual(phase.name, expected)

        phase.name = "Other name"
        self.assertEqual(phase.name, expected)

    def test_is_phase_over(self):
        phase = Phase("Phase name")

        players = MockPlayers(True)
        self.assertTrue(phase.is_phase_over(players))

        players = MockPlayers(False)
        self.assertFalse(phase.is_phase_over(players))

if __name__ == '__main__':
    unittest.main()
