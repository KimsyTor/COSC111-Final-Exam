import unittest
from exercise_7 import word_frequency_counter


class TestWordFrequencyCounter(unittest.TestCase):

    def test_word_frequency_counter(self):
        word_list = ["apple", "banana", "orange",
                     "apple", "grape", "banana", "apple", "orange"]
        result = word_frequency_counter(word_list)
        self.assertEqual(
            result, {'apple': 3, 'banana': 2, 'orange': 2, 'grape': 1})

    def test_word_frequency_counter_with_punctuation(self):
        word_list = ["apple.", "banana", "orange",
                     "apple", "grape", "banana", "apple", "orange!"]
        result = word_frequency_counter(word_list)
        self.assertEqual(result, {'apple.': 1, 'banana': 2,
                                  'orange': 1, 'grape': 1, 'apple': 2, 'orange!': 1})

    def test_word_frequency_counter_with_whitespace(self):
        word_list = ["apple", "banana", "orange ",
                     "apple", "grape", "banana", "apple", "orange"]
        result = word_frequency_counter(word_list)
        self.assertEqual(
            result, {'apple': 3, 'banana': 2, 'orange ': 1, 'grape': 1, 'orange': 1})


if __name__ == '__main__':
    unittest.main()
