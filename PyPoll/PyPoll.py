import os
import csv

total_votes = 0
candidates = {}

# Read in the CSV file
with open(os.path.join('Resources','election_data.csv'), 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # Loop through the data
    for vote in csvreader:
        total_votes += 1 
        voter_id = vote[0]
        county = vote[1] 
        candidate = vote[2]
         
        if candidate in candidates.keys():
          candidates[candidate] += 1
        else:
          candidates[candidate] = 1


print(candidates.values())

          
#List of candidates
print(candidates.keys())

#print(list(candidates.values())/total_votes * 100)

# Winner
print(min(candidates.values())

     
# winner = "" 
# winning_number_of_votes = 0

# for candidate_name in candidates:
#   if candidates[candidate_name] > winning_number_of_votes:
#     winning_number_of_votes = candidates[candidate_name]
#     winner = candidate_name


  (f"---\n"
  f"Election Results\n"
  f"-------------------------\n"
  f"Total Votes: {total_votes}\n"
  f"-------------------------\n")
  
  ("")





  (f"-------------------------\n"
  f"Winner: {max(candidates.Keys())}\n"
  f"-------------------------\n")



with open(os.path.join('Election_Analysis.txt'), 'w') as txtfile:
    txtfile.write(analysis_output)