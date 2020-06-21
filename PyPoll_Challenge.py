# Add dependencies
import csv
import os

# Function to print and save a given message.
# message_to_print: message to be printed
# output_file: file to save the data to
# special_ending: character to be passed to 'end' parameter in print function
def PrintMessage(message_to_print,output_file,special_ending = "\n"):
    print(message_to_print,end=special_ending)
    # Save individual results to the output file
    output_file.write(message_to_print)
    
# Function to loop over data contained in a dictionary to print it out.
# options: dictionary containing name and amount of votes
# total_count: total amount of votes
# output_file: file to save the data to
# Return element -> string containing the most popular among the options 
def PrintIndividualData(options,total_count,output_file) -> str:
    
    # Variable to hold the higher number of votes 
    max_counted = 0 
    # Variable to hold the elemnt with higher votes 
    most_popular = ""
    
    # Loop over the names in the dictionary (keys)
    for element in options.keys():
        # The votes for current element
        votes = options[element]
        # Calculate percentage of votes
        percentage = int(votes) / int(total_count) * 100
        # Message to be printed
        individual_message = f"{element}: {percentage:.1f}% ({int(votes):,})\n"
        # Print out and save the individual results
        PrintMessage(message_to_print=individual_message,output_file=output_file,special_ending="")

        # Check whether current count of votes is higher the previously maximum stored
        if votes > max_counted:
            most_popular = element
            max_counted = votes
    
    # Return value
    return most_popular


# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources","election_results.csv")
# Assign a variable to load a file from a path.
file_to_save = os.path.join("analysis","election_analysis.txt")
# Initialize the total vote counter
total_votes = 0
# Candidates votes
candidates_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

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
        
         # Get county on current row
        county=row[1]
        # Get candidate name on current row
        candidate_name = row[2]

        # Add candidate to the dictionary of candidates if it is his/her first occurrence
        if candidate_name not in candidates_votes.keys():
            # Begin tracking that candidate's vote count. 
            candidates_votes[candidate_name]=0

        # Add a vote to that candidate's count
        candidates_votes[candidate_name]+=1
        
        # Add county to the dictionary of counties if it is its first occurrence
        if county not in counties_turnout.keys():
            # Begin tracking that county's vote count. 
            counties_turnout[county]=0

        # Increment the county turnout by one
        counties_turnout[county]+=1

# Save the results to the output file.
with open(file_to_save,"w") as txt_file:

    # Print out and save the header and total_votes 
    election_results=(
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")    
    PrintMessage(message_to_print=election_results,output_file=txt_file,special_ending="")

    # Print out and save county analysis header
    county_header="\nCounty votes:\n"    
    PrintMessage(message_to_print=county_header,output_file=txt_file,special_ending="")

    # Print the results for each county
    largest_county=PrintIndividualData(options=counties_turnout,total_count=total_votes,output_file=txt_file)
    
    # Print out and save the county with largest turnout
    county_turnout = (
        "\n-------------------------\n"
        f"Largest County Turnout: {largest_county}\n"
        "-------------------------\n")
    PrintMessage(message_to_print=county_turnout,output_file=txt_file,special_ending="")

    # Print the results for each candidate
    winning_candidate = PrintIndividualData(options=candidates_votes, total_count=total_votes, output_file=txt_file)

    # Get the votes of the winning candidate
    winning_count = candidates_votes[winning_candidate]
    # Calculate the percentage of votes of the winning candidate
    winning_percentage = int(candidates_votes[winning_candidate]) / int(total_votes) *100
    
    # Print out and save the winning candidate summary
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    PrintMessage(message_to_print=winning_candidate_summary,output_file=txt_file)


