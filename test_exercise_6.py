import unittest

from exercise_6 import list_to_dict


class TestListToDict(unittest.TestCase):
    def test_list_to_dict(self):
        input_data = [
            ("name", "age", "phone"),
            ("John", 25, 1234567890),
            ("Jane", 24, 9876543210),
            ("Doe", 26, 1234567890),
        ]

        expected_output = [
            {"name": "John", "age": 25, "phone": 1234567890},
            {"name": "Jane", "age": 24, "phone": 9876543210},
            {"name": "Doe", "age": 26, "phone": 1234567890},
        ]

        self.assertEqual(list_to_dict(input_data), expected_output)


if __name__ == "__main__":
    unittest.main()

