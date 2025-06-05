# calgary_dogs.py
# AUTHOR NAME
#
# A terminal-based application for computing and printing statistics based on given input.
# Detailed specifications are provided via the Assignment 4 README file.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.

import pandas as pd


def main():

    # Stage 1: DataFrame Creation
    # Import data here

    df = pd.read_excel('CalgaryDogBreeds.xlsx')
    print("ENSF 692 Dogs of Calgary")

    # Stage 2: User Entry
    # User input stage

    unique_breeds = df["Breed"].unique()  # Get all unique dog breed names

    while True:
        dog_breed_input = input("Please enter a dog breed: ").upper() # makes input uppercase
        try:
            if dog_breed_input in unique_breeds:
                break
            else:
                raise KeyError
        except:
            KeyError("Dog breed not found in the data. Please try again.")

    # Stage 3: Data anaylsis stage 
    # 3.1 Find and print all years where the selected breed was listed in the top breeds.
    totals_per_breed_per_year = df.groupby(['Year', 'Breed'])['Total'].sum()
    print(totals_per_breed_per_year)

if __name__ == '__main__':
    main()
