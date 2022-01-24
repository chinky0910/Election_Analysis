# total number of votes cast
# total number of candidates
# total number of votes received by each caditate
# percentage of vote for each candidate
# candidate who won the election with maximum nyber of votes
import datetime
from random import random
now = datetime.datetime.now()
print("The time right now is ", now)

import csv
dir(csv)

import dict
dir(dict)

import int
dir(int)

import random
dir(random)

file_to_load = 'Resources/election_results.csv'
with open(file_to_load,'r') as election_data:
    print(election_data.read())

import csv
import os
file_to_read = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis","election_analysis.txt")
total_votes=0
with open(file_to_load)as election_data:
    file_reader = csv.reader(election_data) 
    headers = next(file_reader)
    for row in file_reader:
        total_votes += 1
    print (total_votes)
        

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]
        if candidate_name not in candidate_options:
        # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
    # Print the candidate list.
    print(candidate_options)

