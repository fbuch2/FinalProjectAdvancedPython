"""
Script to get a dataset, and clean it and be able to do data analysis on it.
"""
import sys
import pandas as pd
import click

sys.path.append("scripts")
from cleaning_dataset import CleaningDataset
from analysis import Graph


def input_dataset(file):
    """Function to choose the desired dataset."""
    extension = file.rsplit(".", 1)[-1]
    if extension == "csv":
        return pd.read_csv(file)
    raise TypeError(f"The extension is not csv. Got: {extension}")


@click.command(short_help="Parser to import datset")
@click.option("-f", "--filename", required=True, help="File to import")
@click.option(
    "-c",
    "--clean",
    help="Enter Y if you want to clean the dataset.",
)
@click.option(
    "-t",
    "--type",
    help="Enter an S if you want a scatter plot or B if you want a bar chart.",
)
@click.option("--column1", "-1", help="Choose the first variable to analyze")
@click.option("--column2", "-2", help="Chooose the second variable to analyze.")
@click.option("--save_path", "-s", help="Path to save the graphs")
def main(filename, clean, type, column1, column2, save_path):
    """
    Main function
    """
    dataset = input_dataset(filename)
    print(dataset.shape)
    print(dataset.info())

    if clean == "Y":
        dataset = CleaningDataset(dataset).drop_na()
        print(dataset.shape)
        dataset = CleaningDataset(dataset).drop_duplicates()
        print(dataset.shape)

    try:
        if type == "S":
            Graph.visualize_scatter(dataset, column1, column2, save_path)
        elif type == "B":
            Graph.visualize_bar(dataset, column1, save_path)
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
