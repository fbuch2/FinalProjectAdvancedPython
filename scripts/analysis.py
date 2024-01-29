import pandas as pd
import matplotlib.pyplot as plt


class Graph:
    def visualize_numerical_relationship(dataset, column1, column2, save_path=None):
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
            """
            Visualize the relationship between two numerical variables.
            """
            plt.figure(figsize=(8, 6))
            plt.scatter(dataset[column1], dataset[column2])
            plt.title(f"Scatter Plot: {column1} vs {column2}")
            plt.xlabel(column1)
            plt.ylabel(column2)
            plt.show()
        else:
            raise ValueError(f"Both {column1} and {column2} must be numerical columns.")
