"""
Script to obtain graphs from the dataset.
"""

import os
import matplotlib.pyplot as plt


class Graph:
    """
    Class to run the two diferent graphs.
    """

    def visualize_numerical_relationship(dataset, column1, column2, save_path=None):
        """
        Visualize the relationship between two numerical variables.
        """
        valid_columns = [
            "reviews_count",
            "engine_displacement",
            "no_cylinder",
            "seating_capacity",
            "fuel_tank_capacity",
            "rating",
            "starting_price",
            "ending_price",
            "max_torque_nm",
            "max_torque_rpm",
            "max_power_bhp",
            "max_power_rp",
        ]
        if column1 in valid_columns and column2 in valid_columns:
            plt.figure(figsize=(8, 6))
            plt.scatter(dataset[column1], dataset[column2])
            plt.title(f"Scatter Plot: {column1} vs {column2}")
            plt.xlabel(column1)
            plt.ylabel(column2)
            if save_path:
                if not os.path.exists(save_path):
                    os.makedirs(save_path)
                plt.savefig(f"{save_path}/graph.png")
            else:
                plt.show()
        else:
            raise ValueError(f"Both {column1} and {column2} must be numerical columns.")

    def visualize_categorical_distribution(dataset, column1, save_path=None):
        """
        Visualize the distribution of a categorical variable.
        """
        if column1 not in dataset:
            raise ValueError(f"Column '{column1}' does not exist in the dataset.")

        plt.figure(figsize=(8, 6))
        dataset[column1].value_counts().plot(kind="bar", color="skyblue")
        plt.title(f"Distribution of {column1}")
        plt.xlabel(column1)
        plt.ylabel("Count")
        if save_path:
            if not os.path.exists(save_path):
                os.makedirs(save_path)
            plt.savefig(f"{save_path}/graph.png")
        else:
            plt.show()
