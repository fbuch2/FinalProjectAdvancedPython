import sys
import pandas as pd
import click

sys.path.append("scripts")
from cleaning_dataset import CleaningDataset
from analysis import Graph


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
    "-c",
    "--clean",
    help="Enter Y if you want to clean the dataset.",
)
@click.option(
    "--type",
    "-t",
    help="Enter an N if you want numerical or C if you want one one variable of each.",
)
@click.option(
    "--column1", "-1", help="Choose the first variable to analyze"
)
@click.option(
    "--column2", "-2", help="Chooose the second variable to analyze."
)
@click.option(
    "--save_path", "-s", default="output/graph", help="Path to save the graphs"
)
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

    if type == "N":
        if column1 in ['reviews_count' , 'engine_displacement', 'no_cylinder' , 'seating_capacity', 'fuel_tank_capacity' , 'rating' , 'starting_price' , 'ending_price' , 'max_torque_nm' , 'max_torque_rpm' , 'max_power_bhp' , 'max_power_rp']:
            if column1 in ['reviews_count' , 'engine_displacement', 'no_cylinder' , 'seating_capacity', 'fuel_tank_capacity' , 'rating' , 'starting_price' , 'ending_price' , 'max_torque_nm' , 'max_torque_rpm' , 'max_power_bhp' , 'max_power_rp']:
                Graph.visualize_numerical_relationship(dataset, column1, column2) 
            else:
                raise ValueError(f"{column2} is not a numerical column.")
        else:
            raise ValueError(f"{column1} is not a numerical column.")
    



if __name__ == "__main__":
    main()
