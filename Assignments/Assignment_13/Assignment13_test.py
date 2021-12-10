import unittest
import Grades
import math

class Grade_Test(unittest.TestCase):
    def test_total_returns_total_of_list(self):
        
        result = Grades.total([1, 10, 22])
        self.assertEqual(result, 33, "The total function should return 33")
        
    def test_total_returns_0(self):
        result = Grades.total([])
        self.assertEqual()

    def test_average_one(self):
        result - Grades.average([2, 5, 9])
        self.assertAlmostEqual()

    def test_average_two(self):
        result - Grades.average([2, 15, 22, 9])
        self.assertAlmostEqual()

    def teset_average_returns_nan(self):
        result = Grades.average([])
        self.assertIs()

    def test_median_one(self):
        result = Grades.media([2, 5, 1])
        self.assertEqual()

    def test_median_two(self):
        result = Grades.median([5, 2, 1, 3])
        self.assertEqual()

    def test_median_retuns_ValueError(self):
        with self.assertRaises(ValueError):
            result = Grades.median(1)


if __name__ == "__main__":
    unittest.main()
