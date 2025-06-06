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

    df = pd.read_excel('CalgaryDogBreeds.xlsx', index_col = [0,1]) #index by year and month
    # print(df.head(20)) # print for visualization
    print("ENSF 692 Dogs of Calgary")

    # Stage 2: User Entry
    # User input stage

    unique_breeds = df["Breed"].unique()  # Get all unique dog breed names
    # print(unique_breeds)

    # while True:
    #     dog_breed_input = input("Please enter a dog breed: ").strip().upper() # makes input uppercase, strip removes whitespace
    #     try:
    #         if dog_breed_input in unique_breeds:
    #             break
    #         else:
    #             raise KeyError
    #     except:
    #         KeyError(print("Dog breed not found in the data. Please try again."))

    # # Stage 3: Data anaylsis stage 

    dog_breed_input = "LABRADOR RETR"

    # 3.1 Find and print all years where the selected breed was listed in the top breeds.
    # use indexslice to create a dataframe with just the rows of the selected breed
    idx = pd.IndexSlice
    df_breed_rows = df.loc[idx[:, :], :][df['Breed'] == dog_breed_input]
    # create dataframe with selected breed, .index returns multi-index, .get_level_values('Year') returns single index
    # .unique filters for unique years, tolist() converts to a list
    years = df[df['Breed'] == dog_breed_input].index.get_level_values('Year').unique().tolist()
    print("The " + dog_breed_input + " was found in the top breeds for years:", end=" ")
    for year in years:
        print(year, end=" ")

    # 3.2 Calculate and print the total number of registrations of the selected breed found in the dataset.
    total_reg = df_breed_rows['Total'].sum() # sum the totals
    print(f"\nThere have been {total_reg} {dog_breed_input} dogs registered in total.")

    # 3.3 Calculate and print the percentage of selected breed registrations out of the total percentage for each year (2021, 2022, 2023).
    
    for year in [2021, 2022, 2023]:
        total_year_breed = df_breed_rows.loc[year]['Total'].sum()
        total_year_all = df.loc[year]['Total'].sum()
        percentage = total_year_breed / total_year_all * 100
        print(f"The {dog_breed_input} was {percentage:.6f}% of top breeds in {year}")

    # 3.4 Calculate and print the percentage of selected breed registrations out of the total three-year percentage.
    total_breed = df_breed_rows['Total'].sum()
    total_all = df['Total'].sum()
    tot_percentage = total_breed / total_all * 100
    print(f"The {dog_breed_input} was {tot_percentage:.6f}% of top breeds across all years")
    

if __name__ == '__main__':
    main()
