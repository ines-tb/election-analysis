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
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    # Read and analyze the data
    file_reader = csv.reader(election_data)
    
    # Read the headers row
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1
        # Get candidate name on current row
        candidate_name = row[2]
        # Add candidate to the list if it is the first occurrence
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count. 
            candidates_votes[candidate_name]=0

        # Add a vote to that candidate's count
        candidates_votes[candidate_name]+=1
        
# Save the results to the output file.
with open(file_to_save,"w") as txt_file:

    election_results=(
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results,end="")
    # Save final vote count to the output file
    txt_file.write(election_results)

    # Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list.
    for candidate in candidate_options:
        # Retrieve vote count of a candidate
        votes = candidates_votes[candidate]
        # Calculate the percentage of votes
        vote_percentage = int(votes) / int(total_votes) *100

        # Print out each candidate's name, vote count, and percentage of votes
        candidate_result = f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n"
        print(candidate_result)
        # Save candidate result to the output file
        txt_file.write(candidate_result)

        # Determine winning vote count and candidate
        # Determine if the votes are greater than the winning count.
        if votes > winning_count:
            winning_candidate = candidate
            winning_count = votes
            winning_percentage = vote_percentage

    # Printing results
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save winning candidate summary to the output file
    txt_file.write(winning_candidate_summary)

