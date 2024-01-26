import pandas as pd

class DatasetInfo:
    """Class to get information about the dataset"""

    def __init__(self, df):
        self.df = df

    def basic_info(self):
        """
        Display basic information about the dataset.
        """
        print("Basic Information about the Dataset:")
        print(self.df.info())

    def summary_statistics(self):
        """
        Display summary statistics of the numerical columns.
        """
        print("Summary Statistics of Numerical Columns:")
        print(self.df.describe())
