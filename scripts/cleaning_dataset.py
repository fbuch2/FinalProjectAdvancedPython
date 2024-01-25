class CleaningDataset:
    """Class to clean the dataset"""

    def __init__(self, df):
        self.df = df

    # def missing_values(self):
    #    """
    #    Function to count how many null values there are.
    #    """
    #    missing_values = self.df.isnull().sum()
    #    print(f"There are {missing_values} missing values.")

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
