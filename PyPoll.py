### Election Analysis Project

# Add dependencies
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
# 2. A complete list of candidates who received votes.
# 3. The total number of votes each candidate won.
# 4. The percentage of votes each candidate won.
# 5. The winner of the election based on popular vote.


# Assign a variable for the file to load and the path

# direct path
#file_to_load = 'Resources/election_results.csv'

# indirect path method using os
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statment open the file as a text file
#with open(file_to_save, "w") as txt_file:
    
    # Write some data to the file.
    #txt_file.write("Hello World")
    #txt_file.write(f"Counties in the Election\n{'-'*25}\n")
    #txt_file.write("Arapahoe\nDenver\nJefferson")
    #txt_file.write("Denver")
    #txt_file.write("Jefferson")

# Initialize a total vote counter.
total_votes = 0
# Candidate options and candidate votes
candidate_options = []
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file

with open(file_to_load) as election_data:

# election_data = open(file_to_load, 'r')

    # To do: read and analyze the data here.

    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)
    #print(headers)

       # Print each row in the CSV file.
    #for row in file_reader:
        #print(row)

    # Print the file object.
    #print(election_data)



# ANALYSIS

# 1. Total number of votes cast.

# Print each row in the CSV file.
    for row in file_reader:
        # add to the total vote count
        total_votes += 1
        
        # Print the candidate name from each row
        candidate_name = row[2]

        
        # add candidate name to canidate list (if not already there)
        if candidate_name not in candidate_options:
            # Add new/unique candidate name to list
            candidate_options.append(candidate_name)
            
            # Track candidate's vote count
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1    
        
# Header
print("Election Analysis:")
print("\n")

# 1. Print the total votes.
print(f"There are {total_votes:,} total votes reported from the county.")
print("\n")

# 2. Complete list of candidates in the election.
print(f"The candidates in the race are {candidate_options[0]}, \
{candidate_options[1]}, and {candidate_options[2]}.")
print("\n")

# 3. Print each candidate's vote count.
for candidate in candidate_votes:
    print(f"Candidate, {candidate}, has {candidate_votes[candidate]:,} votes.\n")


print("\nElection Summary:\n\n")

# 4. Print candidate name and percentage of votes.
# Iterate through candidate list
for candidate_name in candidate_votes:
    # Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    # Print the candidate name and percentage of votes.
    #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")

    # print each candidate's name, vote count, and percentage of votes.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")


#for candidate_name in candidate_votes:


# 5. Determine the winning vote count and candidate.
# Determine if the votes are greater than the winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):
            # if true then set winning_count = votes and winning percentage =
            # vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # Set the winning_candidate equal to the candidate's name
            winning_candidate = candidate_name

# Winning Candidate Summary
winning_candidate_summary = (
    f"{'-'*25}\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"{'-'*25}\n"
)
print(winning_candidate_summary)

# Using the open() function with the "w" mode we will write data to the file.
#outfile = open(file_to_save, "w")

# Write some data to the file.
#outfile.write("Hello World")

# Close the file
#outfile.close()


# Close the file. (code edited to use 'with' instead of open() and close())
# election_data.close()