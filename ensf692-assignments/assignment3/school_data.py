# school_data.py
# Author: Jason Tieh
#
# A terminal-based application for computing and printing statistics based on given input.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.


import numpy as np
from given_data import year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022

# Declare any global variables needed to store the data here
# Create a dictionary that holds all the school names with the respective school codes.
school_list = [
    0, "Centennial High School", 1224,
    1, "Robert Thirsk School", 1679,
    2, "Louise Dean School", 9626,
    3, "Queen Elizabeth High School", 9806,
    4, "Forest Lawn High School", 9813,
    5, "Crescent Heights High School", 9815,
    6, "Western Canada High School", 9816,
    7, "Central Memorial High School", 9823,
    8, "James Fowler High School", 9825,
    9, "Ernest Manning High School", 9826,
    10, "William Aberhart High School", 9829,
    11, "National Sport School", 9830,
    12, "Henry Wise Wood High School", 9836,
    13, "Bowness High School", 9847,
    14, "Lord Beaverbrook High School", 9850,
    15, "Jack James High School", 9856,
    16, "Sir Winston Churchill High School", 9857,
    17, "Dr. E. P. Scarlett High School", 9858, 
    18, "John G Diefenbaker High School", 9860,
    20, "Lester B. Pearson High School", 9865
]

# You may add your own additional classes, functions, variables, etc.

school_indices = school_list[0::3]  # Extract school indices
school_names = school_list[1::3]  # Extract school names
school_codes = school_list[2::3]  # Extract school codes

# Create two dictionaries to map school names and codes to their respective indices
school_names_dict = dict(zip(school_names, school_indices))
school_code_dict = dict(zip(school_codes, school_indices))

def main():
    # Stage 1 Requirements
    # 1.1 Create a 3-dimensional array using the provided high school enrollment data
    Array = np.array([year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022])
    Array = Array.reshape(10, 20, 3)  # Reshape to (10 years, 20 schools, 3 grades)

    # 1.2 Print the shape and dimensions of the array.
    print("The shape of the array: ", Array.shape) # Should be (10, 20, 3) - 10 years, 20 schools, 3 grades
    print("The dimensions of the array: ", Array.ndim) # 3

    # Stage 2 Requirements: print the following school-specific statistics
    # 2.1 Prompt user for school name or school code
    while True:
        school_input = input("Enter a school name or school code: ")
        try:
            if school_input in school_names_dict:
                school_index = school_names_dict[school_input]
                break
            elif int(school_input) in school_code_dict:
                school_index = school_code_dict[int(school_input)]
                break
            else:
                raise ValueError
        except ValueError:
            print("You must enter a valid school name or code.")

    print("\n***Requested School Statistics***\n")

    # 2.2.1 Print the school name and code
    school_name = school_names[school_index]
    school_code = school_codes[school_index]
    print(f"School Name: {school_name}, School Code: {school_code}")
   
    # 2.2.2 Print the mean enrollment for Grade 10 across all years
    # 2.2.3 Print the mean enrollment for Grade 11 across all years
    # 2.2.4 Print the mean enrollment for Grade 12 across all years
    mean_enrollment = np.mean(Array[:, school_index, :], axis=0)
    print(f"Mean Enrollment for Each Grade 10: {mean_enrollment[0]:.0f}" )
    print(f"Mean Enrollment for Each Grade 11: {mean_enrollment[1]:.0f}" )
    print(f"Mean Enrollment for Each Grade 12: {mean_enrollment[2]:.0f}" )

    # 2.2.5 Print the highest enrollment for across all years
    highest_enrollment = np.nanmax(Array[:, school_index, :])
    print(f"Highest Enrollment for a single grade: {highest_enrollment:.0f}")

    # 2.2.6 Print the lowest enrollment for a single grade within the entire time period
    lowest_enrollment = np.nanmin(Array[:, school_index, :]) 
    print(f"Lowest Enrollment for a single grade: {lowest_enrollment:.0f}")
    
    # 2.2.7 Print the total enrollment for each year from 2013 to 2022
    total_enrollment_per_year = np.sum(Array[:, school_index, :], axis=1)  # axis=1 sums across grades for each year
    for year in range(10):
        print(f"Total enrollment for {2013 + year}: {total_enrollment_per_year[year]:.0f}")

    # 2.2.8 Print the total ten-year enrollment
    total_ten_year_enrollment = np.sum(total_enrollment_per_year)
    print(f"Total ten year enrollment: {total_ten_year_enrollment:.0f}")

    # 2.2.9 Print the mean total yearly enrollment over 10 years
    mean_total_yearly_enrollment = np.mean(total_enrollment_per_year)
    print(f"Mean total enrollment over 10 Years: {mean_total_yearly_enrollment:.0f}")

    # 2.2.10 Print the median value for all enrollments greater than 500
    school_specified_arr = Array[:, school_index, :]  # Extract the data for the specified school
    mask = np.where(school_specified_arr > 500)  # Create a mask for enrollments greater than 500
    enrollments_over_500 = school_specified_arr[mask]  # Apply the mask to get enrollments over 500
    
    # If there are enrollments over 500, calculate and print the median
    if enrollments_over_500.size > 0:
        median_enrollment = np.median(enrollments_over_500)
        print(f"For all enrollments over 500, the median value was: {median_enrollment:.0f}")
    else:
        print("No enrollments over 500.")

    # Stage 3 Requirements: print the following general statistics for all schools
    print("\n***General Statistics for All Schools***\n")

    # 3.1.1 Print the mean enrollment in 2013
    mean_enrollment_2013 = np.nanmean(Array[0])
    print(f"Mean Enrollment in 2013: {mean_enrollment_2013:.0f}")

    # 3.1.2 Print the mean enrollment in 2022
    mean_enrollment_2022 = np.nanmean(Array[9])
    print(f"Mean Enrollment in 2013: {mean_enrollment_2022:.0f}")

    # 3.1.3 Print the total graduating class of 2022 across all schools
    total_graduating_class_2022 = np.nansum(Array[9, :, 2])  # Sum of Grade 12 enrollments in 2022
    print(f"Total graduating class of 2022: {total_graduating_class_2022:.0f}")

    # 3.1.4 Print the highest enrollment for a single grade within the entire time period (across all schools)
    highest_enrollment_all = np.nanmax(Array)  # Max across all years and schools
    print(f"Highest enrollment for a single grade: {highest_enrollment_all:.0f}")

    # 3.1.5 Print the lowest enrollment for a single grade within the entire time period (across all schools)
    lowest_enrollment_all = np.nanmin(Array)  # Min across all years and schools
    print(f"Lowest enrollment for a single grade: {lowest_enrollment_all:.0f}")    

if __name__ == '__main__':
    main()

