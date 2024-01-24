"""
Test if the input is correct
"""

import unittest
from scripts.script import input_dataset

class TestDataset(unittest.TestCase):
    """
    Class to test the input.
    """

    def setUp(self):
        """
        Path to dataset
        """
        self.path = "datasets/CARS_1.casdfsv"

    def test_extensions_fail(self):
        """
        Test for the extensions of the dataset
        """
        with self.assertRaises(TypeError):
            input_dataset(self.path)


if __name__ == "__main__":
    unittest.main()
