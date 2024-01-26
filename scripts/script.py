import sys
import pandas as pd
import click

sys.path.append("scripts")
from cleaning_dataset import CleaningDataset
from info_dataset import DatasetInfo


"""
Script to get a dataset, and clean it and be able to do data analysis on it.
"""


def input_dataset(file):
    """Function to choose the desired dataset."""
    extension = file.rsplit(".", 1)[-1]
    if extension == "csv":
        return pd.read_csv(file)
    raise TypeError(f"The extension is not csv. Got: {extension}")


@click.command(short_help="Parser to import datset")
@click.option("-f", "--filename", required=True, help="File to import")
@click.option(
    "-i",
    "--info",
    help="Enter Y to choose if you want to clear the dataset.",
)
@click.option(
    "-c",
    "--clean",
    help="Enter Y if you want to see more info about the dataset.",
)
def main(filename, clean, info):
    """
    Main function
    """
    dataset = input_dataset(filename)
    print(dataset.shape)
    if info == "Y":
        """Class to find more about the dataset"""
        df = pd.read_csv(filename)
        DatasetInfo(df).basic_info()
        DatasetInfo(df).summary_statistics()

    if clean == "Y":
        dataset = CleaningDataset(dataset).drop_na()
        print(dataset.shape)
        dataset = CleaningDataset(dataset).drop_duplicates()
        print(dataset.shape)


if __name__ == "__main__":
    main()
