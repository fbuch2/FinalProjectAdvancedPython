import pandas as pd
import matplotlib.pyplot as plt


class Graph:
    def visualize_numerical_relationship(dataset, column1, column2, save_path=None):
        """Visualize the relationship between two numerical variables."""
        plt.figure(figsize=(8, 6))
        plt.scatter(dataset[column1], dataset[column2])
        plt.title(f'Scatter Plot: {column1} vs {column2}')
        plt.xlabel(column1)
        plt.ylabel(column2)
        plt.show()

    