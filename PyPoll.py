# -----------------------------------------------------
# Pseoudocode schema:
# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The prrcentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote 
# -----------------------------------------------------

import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources","election_results.csv")
# Assign a variable to load a file from a path.
file_to_save = os.path.join("analysis","election_analysis.txt")
# Initialize the total vote counter
total_votes = 0
# Candidate options
candidate_options = []
# Candidates votes
candidates_votes = {}
# Open the election results and read the file
with open(file_to_load) as election_data:
    # Read and analyze the data
    file_reader = csv.reader(election_data)
    
    # Read the headers row
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:

        candidate_name = row[2]

        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count. 
            candidates_votes[candidate_name]=0

        # Add a vote to that candidate's count
        candidates_votes[candidate_name]+=1
        # Add to the total vote count
        total_votes += 1

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Determine the percentage of votes for each candidate by looping through the counts.
# Iterate through the candidate list.
for candidate in candidate_options:
    # Retrieve vote count of a candidate
    votes = candidates_votes[candidate]
    # Calculate the percentage of votes
    percentage = int(votes) / int(total_votes) *100

    # Print out each candidate's name, vote count, and percentage of votes
    print(f"{candidate}: {percentage:.1f}% ({votes:,})\n")
    
    # Determine winning vote count and candidate
    # Determine if the votes are greater than the winning count.
    if votes > winning_count:
        winning_candidate = candidate
        winning_count = votes
        winning_percentage = percentage

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
