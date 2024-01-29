import unittest
import pandas as pd
import matplotlib.pyplot as plt
from unittest.mock import patch
from scripts.analysis import Graph


class TestVisualizeNumericalRelationship(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        data = {
            'reviews_count': [100, 150, 120, 80, 200],
            'engine_displacement': [1500, 2000, 1800, 2500, 1600],
            'no_cylinder': [4, 6, 4, 6, 4],
            'seating_capacity': [5.0, 7.0, 5.0, 7.0, 5.0],
            'fuel_tank_capacity': [40, 60, 45, 70, 42],
            'rating': [4.5, 4.2, 4.8, 4.0, 4.6],
            'starting_price': [10000, 15000, 12000, 18000, 13000],
            'ending_price': [15000, 20000, 18000, 25000, 19000],
            'max_torque_nm': [180, 220, 200, 250, 190],
            'max_torque_rpm': [2000, 2500, 2200, 2800, 2400],
            'max_power_bhp': [120, 150, 140, 160, 130],
            'max_power_rp': [4000, 4500, 3800, 4200, 3500]
        }
        cls.df = pd.DataFrame(data)

    def test_valid_visualization(self):
        """
        Test if the scatter plot is created for valid numerical columns
        """
        with patch("matplotlib.pyplot.show") as mock_show:
            Graph.visualize_numerical_relationship(
                self.df, 'engine_displacement', 'max_power_bhp'
            )
            mock_show.assert_called_once()

    def test_invalid_column2(self):
        """
        Test if ValueError is raised for an invalid column2
        """
        with self.assertRaises(ValueError):
            Graph.visualize_numerical_relationship(
                self.df, 'engine_displacement', 'test_column'
            )

    def test_invalid_column1(self):
        """
        Test if ValueError is raised for an invalid column1
        """
        with self.assertRaises(ValueError):
            Graph.visualize_numerical_relationship(
                self.df, 'nonexistent_column', 'max_power_bhp'
            )

    def test_invalid_both_columns(self):
        """
        Test if ValueError is raised for invalid column1 and column2.
        """
        with self.assertRaises(ValueError):
            Graph.visualize_numerical_relationship(
                self.df, 'nonexistent_column1', 'nonexistent_column2'
            )


if __name__ == "__main__":
    unittest.main()