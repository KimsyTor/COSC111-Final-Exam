import unittest

from exercise_5 import find_matrix_avg


class TestFindMatrixAvg(unittest.TestCase):
    def test_find_matrix_avg(self):
        # Test case with equal length inner lists
        matrix_equal = [[3, 5, 2], [7, 1, 4], [6, 8, 9]]
        expected_avg_equal = (
            3 + 5 + 2 + 7 + 1 + 4 + 6 + 8 + 9
        ) / 9  # Sum of all elements / Total number of elements

        self.assertAlmostEqual(
            find_matrix_avg(matrix_equal), expected_avg_equal, places=2
        )

        # Test case with unequal length inner lists
        matrix_unequal = [[3, 5, 2], [7, 1], [6, 8, 9, 10]]
        expected_avg_unequal = (
            3 + 5 + 2 + 7 + 1 + 6 + 8 + 9 + 10
        ) / 9  # Sum of all elements / Total number of elements

        self.assertAlmostEqual(
            find_matrix_avg(matrix_unequal), expected_avg_unequal, places=2
        )


if __name__ == "__main__":
    unittest.main()

