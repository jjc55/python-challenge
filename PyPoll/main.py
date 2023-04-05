import os
import csv

election_data = os.path.join('.', 'Resources', 'election_data.csv')

votes = int(0)
candidate_list = []
candidate_votes = {}
 #{name: votes}
 #candidate_votes[name of candidate]=votes --> {name:votes}
with open (election_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)
    
    for index, row in enumerate(csvreader):
        #index = 0, row = 1323913,Jefferson,Charles Casper Stockham
        votes = votes + 1
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
        if row[2] not in candidate_votes:
            candidate_votes[row[2]] = 1
        else:
            candidate_votes[row[2]] = candidate_votes[row[2]] + 1
       
print(f"Election Results")
print(f"-------------------")
print(f"Total Votes: {votes}")
print(f"-------------------")
print(f"{len(candidate_list)}")
    