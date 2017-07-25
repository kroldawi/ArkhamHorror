from unittest import TestCase
from phase import Phase


class TestPhase(TestCase):
    def test_name(self):
        expected = "Phase name"
        phase = Phase(expected)

        self.assertEqual(phase.name, expected)

        phase.name = "Other name"
        self.assertEqual(phase.name, expected)

    def test_is_phase_over(self):
        phase = Phase("Phase name")

        self.assertTrue(phase.is_phase_over())
