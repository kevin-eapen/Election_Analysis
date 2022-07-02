### Election Analysis Project

# Add dependencies
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0
# Candidate options and candidate votes
candidate_options = []
candidate_votes = {}
# Track the winning candidate, vote count, and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # add to the total vote count
        total_votes += 1
        
        # Get candidate name from each row
        candidate_name = row[2]

        # add candidate name to canidate list (if not already there)
        if candidate_name not in candidate_options:
            # Add new/unique candidate name to list
            candidate_options.append(candidate_name)
            
            # Track candidate's vote count
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# Save the reults to our text file
with open(file_to_save, "w") as txt_file:
    # Print the final vote count
    election_results = (
        f"\nElection Results\n"
        f"{'-'*25}\n"
        f"Total Votes: {total_votes:,}\n"
        f"{'-'*25}\n"
    )
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # Iterate through candidate list
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes for the candidate.
        vote_percentage = float(votes) / float(total_votes) * 100
 
        # print each candidate's voter count and percentage of votes.
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        # Save the candidate results to our text file
        txt_file.write(candidate_results)

        # Determine the winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
                # if true then set winning_count = votes and winning percentage = vote_percentage
                winning_count = votes
                winning_percentage = vote_percentage
                # Set the winning_candidate equal to the candidate's name
                winning_candidate = candidate_name

    # Winning Candidate Summary. Print the winning candidate's results.
    winning_candidate_summary = (
        f"{'-'*25}\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"{'-'*25}\n"
    )
    print(winning_candidate_summary)

    # Save the winning candidate's results to the text file
    txt_file.write(winning_candidate_summary)