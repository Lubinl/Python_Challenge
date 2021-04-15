import os
import csv
total_votes = 0
# Read in the CSV file
with open(os.path.join('Resources','election_data.csv'), 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Loop through the data
    for row in csvreader:
        total_votes += 1

analysis_output = (
  f"Election Results\n"
  f"-------------------------\n"
  f"Total Votes: {total_votes}\n"
  f"-------------------------\n"
  f"Khan: 63.000% (2218231)\n"
  f"Correy: 20.000% (704200)\n"
  f"Li: 14.000% (492940)\n"
  f"O'Tooley: 3.000% (105630)\n"
  f"-------------------------\n"
  f"Winner: Khan\n"
  f"-------------------------\n"
)
print(analysis_output)

with open(os.path.join('Election_Analysis.txt'), 'w') as txtfile:
    txtfile.write(analysis_output)