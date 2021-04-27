import os
import csv

#Variables
row_count = 0
previous_profit = 0

#Read CSV file
with open(os.path.join('Resources','budget_data.csv'), 'r') as csvfile:
 # Split the data on commas
   csvreader = csv.reader(csvfile, delimiter=',')
   for row in csvreader:
      row_count = row_count + 1
      profit = (row[1])
      print(profit, previous_profit)
    