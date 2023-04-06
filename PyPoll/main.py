import os
import csv

election_data = os.path.join('.', 'Resources', 'election_data.csv')

votes = int(0)
candidate_list = []
candidate_votes = {}
 #{name: votes}
 #candidate_votes[name of candidate]=votes --> {name:votes}
 #with/as is used for opening files
 
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
            
    max_votes_for = max(candidate_votes, key=candidate_votes.get)
   
    #(".."/PyBank/Analysis/name of file.txt) REMOVE
    with open(os.path.join("Analysis", "Pypoll-output-file.txt"), "w") as textfile:
        textfile.write(f"Election Results \n")
        textfile.write(f"------------------- \n")
        textfile.write(f"Total Votes: {votes} \n")
        textfile.write(f"------------------- \n")     
       
        for key in candidate_votes:
            percentage = (candidate_votes[key]/votes)*100
            percentage2 = ("{:0.3f}" .format(percentage))
            percentage3 = (f"{percentage2}%")
            stored_value = str(f"{key}: {percentage3} ({candidate_votes[key]})")
            textfile.write(f"{stored_value} \n")  
            
        textfile.write(f"------------------- \n")  
        textfile.write(f"Winner: {max_votes_for} \n")