import os
import csv

#Variables
month_count = 0
previous_profit = 0
months = []
profitlosses = []

#Read CSV file
with open(os.path.join('Resources','budget_data.csv'), 'r') as csvfile:
 # Split the data on commas
   csvreader = csv.reader(csvfile, delimiter=',')
   columns_names = next(csvreader)
   for row in csvreader:
      month_count = month_count + 1
      profit = row[1]
      month = row[0]
      months.append(month)
      profitlosses.append(int(profit))
avg_change = sum(profitlosses) / month_count
print(month_count)
print(sum(profitlosses))
print(round(avg_change,2))
print(max(profitlosses))
print(min(profitlosses))
max_index = profitlosses.index(max(profitlosses))
print(max_index)
print(months[max_index])