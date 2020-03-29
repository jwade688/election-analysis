# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

# Add our dependencies
import csv
import os

# Assign a variable for the file to load from the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter
total_votes = 0

# Declare the candidates and the vote dictionary
candidate_options = []
candidate_votes = {}

#Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: perform analysis

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
        
        candidate_votes[candidate_name] += 1

# Save the results to our text file
with open(file_to_save, "w") as txt_file:

    # Print final vote count to the terminal and text file
    election_results = (
        f"\nElection Results\n"
        f"----------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"----------------------------\n")
    print(election_results, end="")
    # Save final vote count to the text file
    txt_file.write(election_results)

    

    # Determine and print the percentage of votes for each candidate by looping through the count
    # Iterate through the candidate list
    for candidate in candidate_votes:
        # Retrieve the vote count for each candidate
        votes = candidate_votes[candidate]
        # Calculate the percentage for each candidate
        vote_percentage = float(votes) / float(total_votes) * 100

        #Print each candidates name, vote count, and percentage of votes to terminal
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)

        #Determine the winning vote count and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate 

    # Print the winning candidates' results to the terminal.
    winning_candidate_summary = (
        f"------------------------\n"
        f"Winner = {winning_candidate}\n"
        f"Winning vote count: {winning_count:,}\n"
        f"Winning percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    # print(winning_candidate_summary)
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
            


