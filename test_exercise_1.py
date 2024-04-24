import unittest

from exercise_1 import time_converter


class test_convert_time(unittest.TestCase):
    def test_time_converter(self):
        self.assertEqual(time_converter('12:30'), '12:30 p.m.')
        self.assertEqual(time_converter('09:00'), '9:00 a.m.')
        self.assertEqual(time_converter('23:15'), '11:15 p.m.')
        self.assertEqual(time_converter('00:45'), '12:45 a.m.')


if __name__ == '__main__':
    unittest.main()
