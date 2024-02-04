"""
Script to clean the dataset if chosen to do so.
"""


class CleaningDataset:
    """Class to clean the dataset"""

    def __init__(self, df):
        self.df = df

    def drop_na(self):
        """
        Function that drops the rows with null values.
        """
        self.df = self.df.dropna()
        return self.df

    def drop_duplicates(self):
        """
        Function that drops the duplicated rows.
        """
        self.df = self.df.drop_duplicates()
        return self.df
