#import packages
import os
import csv
#creation of variables/lists/Value Holder
total_votes = 0
votes = []
candidates = []
#Read in the CSV file
with open(os.path.join('Resources','election_data.csv'), 'r') as csvfile:

    #Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    #Skips header
    header = next(csvreader)

    #Loop through the data
    for vote in csvreader:
        #Counts votes
        total_votes = total_votes + 1 
        #Candidate column       
        candidate = vote[2]
        #Creation of new variable  
        if candidate in candidates:
          candidate_names = candidates.index(candidate)
          votes[candidate_names] = votes[candidate_names] + 1
        else:
          candidates.append(candidate)
          votes.append(1)
 #Election Metrics
candidate_dist_of_votes = []
total_tally = 0
total_number_of_votes = votes[0]
#Loop through numbers in candidadates list
for vote_tally in range(len(candidates)):
  #Formula to identify candidate voter distribution
  vote_dist = votes[vote_tally]/total_votes*100
  candidate_dist_of_votes.append(vote_dist)
  #Loop used to identify 
  if votes[vote_tally]> total_number_of_votes:
    total_number_of_votes = votes[vote_tally]
    total_tally = vote_tally
#Identify winner of election
winner = candidates[total_tally]
#Round percentages
candidate_dist_of_votes = [round(i,2) for i in candidate_dist_of_votes]
#Collect output into results
results = []
results.append(f"Election Results\n-------------------------")
results.append(f"Total Votes: {total_votes}\n-------------------------")
for vote_tally in range(len(candidates)):
  print(f"{candidates[vote_tally]}: {candidate_dist_of_votes[vote_tally]}00% ({votes[vote_tally]})")
  results.append(f"{candidates[vote_tally]}: {candidate_dist_of_votes[vote_tally]}00% ({votes[vote_tally]})")
results.append(f"-------------------------\nWinner: {winner}\n-------------------------")
#Write output into text file with use of loop
with open(os.path.join('Analysis','Election_Analysis.txt'), 'w') as txtfile:
  for result in results:
    print(result)
    txtfile.write(result + '\n')