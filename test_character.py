import unittest
from character import Character


NAME = "Joe Diamond"
PROFESSION = "Private Eye"
MAX_STAMINA = 6
MAX_SANITY = 4
FOCUS = 3


class TestCharacter(unittest.TestCase):
    def test_basic_properties(self):
        character = Character(NAME, PROFESSION, MAX_STAMINA, MAX_SANITY, FOCUS)

        self.assertEqual(character.name, NAME)
        self.assertEqual(character.profession, PROFESSION)
        self.assertEqual(character.max_stamina, MAX_STAMINA)
        self.assertEqual(character.max_sanity, MAX_SANITY)
        self.assertEqual(character.focus, FOCUS)
        self.assertEqual(character.stamina, MAX_STAMINA)
        self.assertEqual(character.sanity, MAX_SANITY)

        character.name = "John Doe"
        character.max_stamina = 100
        character.max_sanity = 100

        self.assertEqual(character.name, NAME)
        self.assertEqual(character.max_stamina, 100)
        self.assertEqual(character.max_sanity, 100)

        character.max_sanity = -1
        character.max_stamina = -1
        self.assertEqual(character.max_sanity, 0)
        self.assertEqual(character.max_stamina, 0)

if __name__ == '__main__':
    unittest.main()