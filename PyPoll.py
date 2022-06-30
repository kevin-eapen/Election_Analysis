### Election Analysis Project

import csv
# import random
# import datetime
import os

# dir() function will return all functions/attributes/methods available for 
# whatever module, variable, or data type you pass into dir(). Here we pass csv, 
# to output all the functions available to the 'csv' module. 
# dir(csv)

# dir() skill drill: find all attributes/methods for the following
# 1. int 2. float 3. bool 4. list 5. tuple 6. dict 7. datetime
# bonus: numpy(omitted bc I don't have numpy lib installed rn), random
"""
dir(int)
dir(float)
dir(bool)
dir(list)
dir(tuple)
dir(dict)
dir(datetime)
dir(random)
"""
# dir(os)
# dir(os.path)

# The data we need to retrieve.
# 1. The total number of votes cast.
# 2. A complete list of cnadidates who received votes.
# 3. The percentage of votes each candidate won.
# 4. The total number of votes each candidate won.
# 5. The winner of the election based on popular vote.


# Assign a variable for the file to load and the path

# direct path
#file_to_load = 'Resources/election_results.csv'

# indirect path method using os
file_to_load = os.path.join("Resources", "election_results.csv")

# Open the election results and read the file

with open(file_to_load) as election_data:

# election_data = open(file_to_load, 'r')

    # To do: read and analyze the data here.

    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print(headers)

       # Print each row in the CSV file.
    for row in file_reader:
        print(row)

    # Print the file object.
    #print(election_data)

# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statment open the file as a text file
#with open(file_to_save, "w") as txt_file:


    
    # Write some data to the file.
    #txt_file.write("Hello World")
    #txt_file.write(f"Counties in the Election\n{'-'*25}\n")
    #txt_file.write("Arapahoe\nDenver\nJefferson")
    #txt_file.write("Denver")
    #txt_file.write("Jefferson")

# Using the open() function with the "w" mode we will write data to the file.
#outfile = open(file_to_save, "w")

# Write some data to the file.
#outfile.write("Hello World")

# Close the file
#outfile.close()


# Close the file. (code edited to use 'with' instead of open() and close())
# election_data.close()