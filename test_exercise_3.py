import unittest
from exercise_3 import max_digit


class test_exercise_3(unittest.TestCase):
    def test_time_converter(self):
        self.assertEqual(max_digit(0), 0)
        self.assertEqual(max_digit(52), 5)
        self.assertEqual(max_digit(634), 6)
        self.assertEqual(max_digit(10000), 1)


if __name__ == '__main__':
    unittest.main()
