#Imports dependencies
import os
import csv

#Specifies where CSV file is located and assigns to variable "election_data"
election_data = os.path.join('.', 'Resources', 'election_data.csv')

#Initializes different variables that will be used later in the code
votes = int(0)
candidate_list = []
candidate_votes = {}

#Opens election_data as a read only file as variable name "csvfile", makes sure the csvfile is read 
#with a comma being the delimiter, and stores the header informtion in variable name "csv_header" 
with open (election_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)

#Iterates through the rows in csvreader and records the candidates' names in a list, the number 
# of votes per candidate, and the candidate with the most number of votes
    for index, row in enumerate(csvreader):
        votes = votes + 1
        if row[2] not in candidate_list:
            candidate_list.append(row[2])    
        if row[2] not in candidate_votes:
            candidate_votes[row[2]] = 1
        else:
            candidate_votes[row[2]] = candidate_votes[row[2]] + 1
            
    max_votes_for = max(candidate_votes, key=candidate_votes.get)
   
#Creates and writes output in "Pypoll-out-file.txt" within the Analysis folder
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