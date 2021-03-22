# Import 'csv' and 'os' modules
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_results.txt")

# Initialize a total vote counter.
total_votes = 0
# Initialize candidate and county options
candidate_options = []
county_options = []
# Initialize candidate votes and county votes dictionary
candidate_votes = {}
county_votes = {}

# Winning Candidate, Winning Count, Highest County Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
highest_turnout = ""
cwinning_count = 0
cwinning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        
        # Print the candidate name and county for each row
        candidate_name = row[2]
        county_name = row[1]

        # Find list of candidates
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)

            # Begins tracking that candidate's vote count
            candidate_votes[candidate_name] = 0 

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

        # Find list of counties
        if county_name not in county_options:
            # Add the county name to the county list
            county_options.append(county_name)

            #Begins tracking that county's turnout
            county_votes[county_name] = 0

        #Add a vote to that county's count.
        county_votes[county_name] += 1

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

    county_turnout = (
        f"\nCounty Votes\n")

    print(county_turnout, end="")
    # Save the county turnout header to the text file
    txt_file.write(county_turnout)

    # Determine the percentage of votes for each county by looping through the counts.
    # Use a loop to iterate through the county list
    for counties in county_options:
        # Retrieve the votes of the candidate from county_votes dictionary
        cvotes = county_votes[counties]
        cvote_percent = float(cvotes) / float(total_votes) * 100

        county_results = (f'{counties}: {cvote_percent:.1f}% ({cvotes:,})\n')
        # Print out each county name, percentage of votes in that county, and total votes in the county to the terminal
        print(county_results)
        # Save the county results to the text file
        txt_file.write(county_results)
        # Print out the county with the highest turnout
        if (cvotes > cwinning_count) and (cvote_percent > cwinning_percentage):
            cwinning_count = cvotes
            cwinning_percentage = cvote_percent
            highest_turnout = counties

    
    highest_turnout_summary = (
        f"\n-------------------------\n"
        f"Largest County Turnout: {highest_turnout}\n"
        f"-------------------------\n")

    # Print the county with highest turnout to terminal
    print(highest_turnout_summary)
    # Save the county with the highest turnout to the text file
    txt_file.write(highest_turnout_summary)

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
        # Print out each candidate's name, vote count, and percentage of winning candidate
        if (votes > winning_count) and (vote_percent > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percent
            winning_candidate = candidates

    
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

    