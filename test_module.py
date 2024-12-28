import unittest
from mean_var_std import calculate

class TestStatistics(unittest.TestCase):
    
    def test_calculate(self):
        # Test the example given in the prompt
        result = calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(result, {
            'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
            'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
            'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
            'max': [[6, 7, 8], [2, 5, 8], 8],
            'min': [[0, 1, 2], [0, 3, 6], 0],
            'sum': [[9, 12, 15], [3, 12, 21], 36]
        })

    def test_value_error(self):
        # Test when the list has fewer or more than 9 numbers
        with self.assertRaises(ValueError):
            calculate([1, 2, 3, 4, 5, 6, 7])  # Only 7 elements

        with self.assertRaises(ValueError):
            calculate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # 10 elements

    def test_mean(self):
        # Test the mean calculation for different axes and flattened
        result = calculate([1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(result['mean'][0], [4.0, 5.0, 6.0])  # mean for columns
        self.assertEqual(result['mean'][1], [2.0, 5.0, 8.0])  # mean for rows
        self.assertEqual(result['mean'][2], 5.0)  # mean for the flattened array

    def test_variance(self):
        # Test the variance calculation
        result = calculate([1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(result['variance'][0], [6.0, 6.0, 6.0])  # variance for columns
        self.assertEqual(result['variance'][1], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666])  # variance for rows
        self.assertEqual(result['variance'][2], 6.666666666666667)  # variance for flattened array

    def test_standard_deviation(self):
        # Test the standard deviation calculation
        result = calculate([1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(result['standard deviation'][0], [2.449489742783178, 2.449489742783178, 2.449489742783178])  # standard deviation for columns
        self.assertEqual(result['standard deviation'][1], [0.816496580927726, 0.816496580927726, 0.816496580927726])  # standard deviation for rows
        self.assertEqual(result['standard deviation'][2], 2.581988897471611)  # standard deviation for flattened array

    def test_max(self):
        # Test the max calculation
        result = calculate([1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(result['max'][0], [7, 8, 9])  # max for columns
        self.assertEqual(result['max'][1], [3, 6, 9])  # max for rows
        self.assertEqual(result['max'][2], 9)  # max for flattened array

    def test_min(self):
        # Test the min calculation
        result = calculate([1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(result['min'][0], [1, 2, 3])  # min for columns
        self.assertEqual(result['min'][1], [1, 4, 7])  # min for rows
        self.assertEqual(result['min'][2], 1)  # min for flattened array

    def test_sum(self):
        # Test the sum calculation
        result = calculate([1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(result['sum'][0], [12, 15, 18])  # sum for columns
        self.assertEqual(result['sum'][1], [6, 15, 24])  # sum for rows
        self.assertEqual(result['sum'][2], 45)  # sum for flattened array

if __name__ == '__main__':
    unittest.main()
