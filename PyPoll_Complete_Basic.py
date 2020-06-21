
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

# List of counties
counties_list = []
# County name and vote cast
counties_turnout = {}
# Name of the county with largest tournout
largest_county = ""
# Number of votes in the counter with largest tournout
max_county_votes = 0

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

        # Get county on current row
        county=row[1]

        # Add candidate to the list if it is his/her first occurrence
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count. 
            candidates_votes[candidate_name]=0

        # Add a vote to that candidate's count
        candidates_votes[candidate_name]+=1
        
        # Add county to the list if it is its first occurrence
        if county not in counties_list:
            counties_list.append(county)
            counties_turnout[county]=0

        # Increment the county turnout by one
        counties_turnout[county]+=1

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

    # Print out the header for the counties results
    county_header="\nCounty votes:\n"
    print(county_header,end="")
    # Save county analysis header to the output file
    txt_file.write(county_header)

    # Loop over the counties and their cast to print out the results
    for county in counties_list:
        # The votes in current county
        votes = counties_turnout[county]
        # Calculate individual county percentage of votes
        county_percentage = int(votes) / int(total_votes) * 100
        # Print out the county results
        county_result = f"{county}: {county_percentage:.1f}% ({int(votes):,})\n"
        print(county_result,end="")
        # Save individual county results to the output file
        txt_file.write(county_result)

        # Check whether current count has more votes than the previously more participating stored
        #   this means the current county turnout is bigger than any previous found
        if votes > max_county_votes:
            largest_county = county
            max_county_votes = votes
    
    # Print county with largest turnout
    county_turnout = (
        "\n-------------------------\n"
        f"Largest County Turnout: {largest_county}\n"
        "-------------------------\n")
    print(county_turnout,end="")
    # Save county largest turnout to the output file
    txt_file.write(county_turnout)

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

    # Printing winner results
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save winning candidate summary to the output file
    txt_file.write(winning_candidate_summary)

