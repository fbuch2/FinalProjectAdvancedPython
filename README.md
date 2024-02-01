# FinalProjectAdvancedPython
This is my final project for advanced python

## Table of contents

- Functions of the script
- Installation
- Testing
- Usage
- Linting

## Functions of the script
The main goal of this script is to take a dataset, clean it and then obtain a graph with one or two of the chosen columns.
A scatter plot can be obtained for two numerical variables or a bar plot for one variable.

## Installation
To install the requirements it can be done by either entering one of the two command lines found below:
    
    pip install -r requirements.txt
or
    
    make install

## Testing
The scripts have a total of 11 tests that can be tested by either using pytest or unittest. They can be activated in the following way:

    make test
    make unittest
or, if desired
 pytest
 python -m unittest

## Linting
To lint the code the main tool used was flake8. To check that you can put enter in the command line (this will ignore the ony error that coulnd't be solved)
    
    make flake8 scripts
Also, if desired, pylint can be used to checck the linting:

    pylint scripts
## Usage
As said, the script can be used to obtain two types of graphs. To do se there are the folllwing commands that can be selected using click:
    
    -f datasets/CARS_1.csv
    
    -c Y

    -t S
    -t B

    -1 fuel_tank_capacity
    -1 body_type

    -2 ending_price

    -s output
- f, or filename is where the selected dataset goes.
- c, or clean allows the option to decide if the dataset wants to be cleaned up or not(delete duplicates and null values). To activate it write Y.
- t, or type allows to choose between the scatter graph (S) or the bar plot (B).
- 1, or column1 is the place to input, in the case of the bar graph the chosen column, or for the scatter plot the first variable (has to be numerical).
- 2, or column2 is where the second chosen column for the scatter plot goes (has to be numerical).
- s, or save_file stands for the folder where the graph wants to be saved. This option can either be selected or not. If not, the graph will be displayed. If the selected folder doesn't exist it will be created.

### Examples

Here multiple example of codes to run can be found:

To obtain a scatter plot, clean the dataset and save the graph:

    python scripts/script.py -f datasets/CARS_1.csv -c Y -t S -1 fuel_tank_capacity -2 ending_price -s output
To obtain a bar graph without saving the graph neither cleaning the dataset:

    python scripts/script.py -f datasets/CARS_1.csv -t B -1 body_type
