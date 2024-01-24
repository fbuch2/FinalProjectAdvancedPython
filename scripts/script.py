"""
Script to get a dataset, and clean it and be able to do data analysis on it.
"""
import sys
sys.path.append("scripts")
import pandas as pd
import click


def input_dataset(file):
    """Function to choose the desired dataset."""
    extension = file.rsplit(".", 1)[-1]
    if extension == "csv":
        return pd.read_csv(file)
    else:
        raise TypeError(f"The extension is not csv. Got: {extension}")

    

@click.command(short_help="Parser to import datset")
@click.option("-f", "--filename", required=True, help="File to import")

def main(filename):
    """
    Main function
    """
    dataset = input_dataset(filename)
    print(dataset.shape)

if __name__ == "__main__":
    main()