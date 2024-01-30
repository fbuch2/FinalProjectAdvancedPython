import unittest
import pandas as pd
from scripts.cleaning_dataset import CleaningDataset

"""
Test if the cleaning dataset functions work correctly
"""

class TestCleaningDataset(unittest.TestCase):

    def setUp(self):
        # Create a sample DataFrame for testing
        data = {
            'col1': [1, 2, 3, 4, 5, None],
            'col2': ['A', 'B', 'C', 'A', 'B', 'C'],
            'col3': [1.1, 2.2, 3.3, 4.4, 5.5, 6.6]
        }
        self.df = pd.DataFrame(data)
        self.cleaner = CleaningDataset(self.df.copy())

    def test_drop_na(self):
        self.cleaner.drop_na()
        self.assertTrue(self.cleaner.df.notna().all().all())

    def test_drop_duplicates(self):
        self.cleaner.drop_duplicates()
        self.assertTrue(self.cleaner.df.duplicated().sum() == 0)

    def test_initialization(self):
        self.assertIsNotNone(self.cleaner.df)
        self.assertIsInstance(self.cleaner.df, pd.DataFrame)

if __name__ == '__main__':
    unittest.main()
