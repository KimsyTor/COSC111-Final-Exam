import unittest
from exercise_4 import count_vowels


class TestCountVowels(unittest.TestCase):

    def test_count_vowels(self):
        self.assertEqual(count_vowels("Hello, World!"), 3)
        self.assertEqual(count_vowels("Python is awesome"), 6)
        self.assertEqual(count_vowels(
            "The quick brown fox jumps over the lazy dog"), 11)
        self.assertEqual(count_vowels("AaEeIiOoUu"), 10)
        self.assertEqual(count_vowels(""), 0)
        self.assertEqual(count_vowels("1234567890"), 0)
        self.assertEqual(count_vowels(
            " !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"), 0)


if __name__ == '__main__':
    unittest.main()
