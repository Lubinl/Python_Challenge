import os
import csv

#Variables
month_count = 0
previous_profit = 0
totalchange = 0
maxinc = 0
maxdec = 0
months = []
profitlosses = []
maxincdate = ''
maxdecdate = ''
#Read CSV file
with open(os.path.join('Resources','budget_data.csv'), 'r') as csvfile:
 # Split the data on commas
   csvreader = csv.reader(csvfile, delimiter=',')
   columns_names = next(csvreader)
   for row in csvreader:
      month_count = month_count + 1
      profit = int(row[1])
      if month_count > 1:
         change = profit - previous_profit
         totalchange = totalchange + change
         if change > maxinc:
            maxinc = change
            maxincdate = row[0]
         if change < maxdec:
            maxdec = change
            maxdecdate = row[0]
      profitlosses.append(int(profit))
      previous_profit = profit
avg_change = totalchange / (month_count-1)
print(month_count)
print(sum(profitlosses))
print(round(avg_change,2))
print(maxinc)
print(maxincdate)
print(maxdec)
print(maxdecdate)

  ```text
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)
  ```