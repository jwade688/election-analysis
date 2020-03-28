# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates and counties that received votes
# 3. The number of votes and percentage of votes for each county
# 4. The county with the largest turnout
# 4. The percentage and total number of votes each candidate won
# 5. The winner of the election based on popular vote.

# Add our dependencies
import csv
import os

# Assign a variable for the file to load and file to save.
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")



# DECLARE NECESSARY VARIABLES
# Initialize a total vote counter
total_votes = 0

# Declare the candidates and county list and tvote dictionary
candidate_options = []
candidate_votes = {}
county_options = []
county_votes = {}

#Winning County and Winning County Tracker
winning_county = ""
winning_county_count = 0

#Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_candidate_count = 0
winning_candidate_percentage = 0


#DETERMINE THE TOTAL VOTES, CANDIDATES WITH VOTES, AND COUNTIES WITH VOTES
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function
    file_reader = csv.reader(election_data)
    # Print the header row
    headers = next(file_reader)

    # Print each row in the CSV file
    for row in file_reader:
        # Add to the total vote counter
        total_votes += 1

        # Print the candidate name for each row
        candidate_name = row[2]

        # Add the name to the candidate list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            # Set each candidate in dictionary vote count to 0
            candidate_votes[candidate_name] = 0
        
        # Otherwise, tally the votes for each candidate
        candidate_votes[candidate_name] += 1

        # Print the county name for each row
        county_name = row[1]

        # Add the county name to the county list
        if county_name not in county_options:
            county_options.append(county_name)
            # Set each candidate in dictionary county count to 0
            county_votes[county_name] = 0
        
        # Otherwise, tally the votes for each county
        county_votes[county_name] += 1

# Save the results to our text file
with open(file_to_save, "w") as txt_file:

    # Print final vote count to the terminal and text file
    election_results = (
        f"\nElection Results\n"
        f"----------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"----------------------------\n\n")
        
    print(election_results, end="")
    # Save final vote count to the text file
    txt_file.write(election_results)

    # Determine and print the voting percentage for each county by looping through the count

    # Print header for the the county votes in the terminal and text file
    print(f"County Votes:\n")
    txt_file.write(f"County Votes:\n")

    # Determine and print the percentage of votes for each county by looping through the count
    # Iterate through the county list
    for county in county_votes:
        # Retrieve the vote count for each county
        votes = county_votes[county]
        # Calculate the percentage for each county
        county_percentage = float(votes) / float(total_votes) * 100

        #Print each county's name, percentage of votes, and vote count to the terminal and text file
        county_results = (f"{county}: {county_percentage:.1f}% ({votes:,})\n")
        print(county_results)
        txt_file.write(county_results)

        #Determine the winning county count and county
        if (votes > winning_county_count):
            winning_county_count = votes
            winning_county = county
    
    # Print the largest county turnout results to the terminal and text file.
    winning_county_summary = (
        f"\n------------------------\n"
        f"Largest County Turnout: {winning_county}\n"
        f"-------------------------\n")
    print(winning_county_summary)
    txt_file.write(winning_county_summary)


    # Determine and print the percentage of votes for each candidate by looping through the count
    # Iterate through the candidate list
    for candidate in candidate_votes:
        # Retrieve the vote count for each candidate
        votes = candidate_votes[candidate]
        # Calculate the percentage for each candidate
        vote_percentage = float(votes) / float(total_votes) * 100

        #Print each candidates name, vote count, and percentage of votes to terminal and text file
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)


        #Determine the winning vote count and candidate
        if (votes > winning_candidate_count) and (vote_percentage > winning_candidate_percentage):
            winning_candidate_count = votes
            winning_candidate_percentage = vote_percentage
            winning_candidate = candidate 

    # Print the winning candidates' results to the terminal and text file.
    winning_candidate_summary = (
        f"------------------------\n"
        f"Winner = {winning_candidate}\n"
        f"Winning vote count: {winning_candidate_count:,}\n"
        f"Winning percentage: {winning_candidate_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
