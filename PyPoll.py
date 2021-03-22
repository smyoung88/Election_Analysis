# Import 'csv' and 'os' modules
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0
# Initialize candidate options
candidate_options = []
# Initialize candidate votes dictionary
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        
        # Print the candidate name for each row
        candidate_name = row[2]

        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)

            # Begins tracking that candidate's vote count
            candidate_votes[candidate_name] = 0 

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

#Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print Total Votes to the terminal
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")

    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
    # Determine the percentage of votes for each candidate by looping through the counts.
    # Use a loop to iterate through cadidate list
    for candidates in candidate_options:
        # Retrieve the votes of the candidate from candidate_votes dictionary
        votes = candidate_votes[candidates]
        vote_percent = float(votes) / float(total_votes) * 100

        candidate_results = (f'{candidates}: {vote_percent:.1f}% ({votes:,})\n')
        # Print out each candidate's name, vote count, and percentage of votes to the terminal
        print(candidate_results)
        # Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # To-do: print out each candidate's name, vote count, and percentage of winning candidate
        if (votes > winning_count) and (vote_percent > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percent
            winning_candidate = candidates

    # Print the winning candidates' results to the terminal
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    # Print the winning candidate's results to the terminal
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)

# Print the candidate list
# print(candidate_options)
# Print the total votes.
# print(total_votes)
# Print candidate votes
# print(candidate_votes)


# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5 . The winner of the election based on popular vot