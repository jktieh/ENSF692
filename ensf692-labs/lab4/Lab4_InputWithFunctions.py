# ENSF 692 Spring 2025
# May 15 Lab 4
# Input With Functions

# Add comments to explain the functionality of this program

# This program demonstrates how to use functions to get user input and process it.
def get_user_input(n):
    entry = input("Please type any entry #" + str(n + 1) + ": ") # n + 1 since range starts at 0
    return entry, type(entry)

# This function processes the user input and prints the entry and its type.
def process_user_input(n, entry, type):
    print("This is entry #" + str(n + 1) + ":", entry)
    print("The type of entry #" + str(n + 1) + " is :", str(type))


print('\n' * 2)
num_of_repeats = 3
results = []
results_types = []

# this function is called based on the number of repeats defined above, which is 3
# a returns the entry, b returns the type of entry
for i in range(num_of_repeats):
    a, b = get_user_input(i)
    results.append(a)
    results_types.append(b)

# this is used to print the results
for i in range(num_of_repeats):
    process_user_input(i,results[i], results_types[i])
