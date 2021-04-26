# Import packages
import os
import csv

#Read CSV file
with open(os.path.join('Resources','budget_data.csv'), 'r') as csvfile:

 # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    #header = next(csvreader)
    #print(csvreader)

    # csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")
    
    # for row in csvreader:
    #     print(row)