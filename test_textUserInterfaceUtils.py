from unittest import TestCase
from textUserInterfaceUtils import TextUserInterfaceUtils as Utils


class test_textUserInterfaceUtils(TestCase):

    def test_add_text(self):
        expected = "aabc"

        result = Utils.add_text("a", 2) + Utils.add_text("b", 1) + Utils.add_text("c", 1)
        self.assertEqual(result, expected)

        result = Utils.add_text("aabc", 1)
        self.assertEqual(result, expected)

    def test_add_text_spaced_single_occurrence(self):
        expected = "a "

        result = Utils.add_text_spaced("a")
        self.assertEqual(result, expected)

    def test_add_text_spaced(self):
        expected = "a a b c "

        result = Utils.add_text_spaced("a", 2) + Utils.add_text_spaced("b", 1) + Utils.add_text_spaced("c", 1)
        self.assertEqual(result, expected)

    def test_create_h1(self):
        header = "Zi dupa zi"
        expected = ". . . * * * * " + header + " * * * * . . . "

        result = Utils.create_h1(header)

        self.assertEqual(result, expected)

    def test_add_asterisk(self):
        qty = 10

        result = Utils.add_asterisk(10)

        self.assertTrue(len(result), qty)
        self.assertEqual(result.count("*"), qty)
