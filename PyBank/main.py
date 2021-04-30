#import packages
import os
import csv

#Creation of Variables/List/Value Holders
month_count = 0
previous_profit = 0
totalchange = 0
maxinc = 0
maxdec = 0
profitlosses = []
maxincdate = ''
maxdecdate = ''
#Read CSV file
with open(os.path.join('Resources','budget_data.csv'), 'r') as csvfile:
 # Split the data on commas
   csvreader = csv.reader(csvfile, delimiter=',')
   columns_names = next(csvreader)
   #Loop throughfile
   for row in csvreader:
      #Total number of months in file
      month_count = month_count + 1
      #Identify locaiton of profit values
      profit = int(row[1])
      #Conditonal statement
      if month_count > 1:
         change = profit - previous_profit
         totalchange = totalchange + change
         if change > maxinc:
            maxinc = change
            maxincdate = row[0]
         if change < maxdec:
            maxdec = change
            maxdecdate = row[0]
      #Add profit values to Profit/Loss list
      profitlosses.append(int(profit))
      previous_profit = profit
#Formula used to identify average change in profit
avg_change = totalchange / (month_count-1)
#Create list to collect output
results = []
results.append(f'Financial Analysis')
results.append(f'----------------------------')
results.append(f'Total Months: {month_count}')
results.append(f'Total: ${sum(profitlosses)}')
results.append(f'Average  Change: ${round(avg_change,2)}')
results.append(f'Greatest Increase in Profits: {maxincdate} (${maxinc})')
results.append(f'Greatest Decrease in Profits: {maxdecdate} (${maxdec})')
#Write output into textfile using loop
with open(os.path.join('Analysis','Budget Data Analysis.txt'), 'w') as txtfile:
  for result in results:
    print(result)
    txtfile.write(result + '\n')