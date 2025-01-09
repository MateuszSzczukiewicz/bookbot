import unittest
from main import words_count, letter_count


class TextTextAnalysis(unittest.TestCase):
    def test_words_count(self):
        """Test the words_count function."""
        self.assertEqual(words_count("Hello world"), 2)
        self.assertEqual(words_count(""), 0)
        self.assertEqual(words_count("One two three four"), 4)

    def test_letter_count(self):
        """Test the letter_count function."""
        self.assertEqual(letter_count("aabbcc"), {"a": 2, "b": 2, "c": 2})
        self.assertEqual(letter_count("AaaBbb"), {"a": 3, "b": 3})
        self.assertEqual(letter_count("123 !@#"), {})
        self.assertEqual(
            letter_count("Hello, World!"),
            {"h": 1, "e": 1, "l": 3, "o": 2, "w": 1, "r": 1, "d": 1},
        )


if __name__ == "__main__":
    unittest.main()
