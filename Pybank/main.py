#create file paths across operating systems
import os

#module for reading csv files
import csv

budget_csv = os.path.join('Resources', 'budget_data.csv')

#read using csv module
with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    
    #pull out column names and store data in lists
    csv_header = next(csvreader)
    
    month = []
    profit_loss = []
    profit_loss_change = []
    monthly_change = []
    
    #read each row of data and append
    for row in csvreader:
        month.append(row[0])
        profit_loss.append(row[1])
    print(f"Total Months:{len(month)}")

#find net total profit/losses
profit_loss_int = map(int,profit_loss)
net_total = sum(profit_loss_int)
print(f"Net Total Profit/Losses:{net_total}")

#find monthly average change in profit/losses
x = 0
for x in range(len(profit_loss) - 1):
    change = int(profit_loss[x+1]) - int(profit_loss[x])
    profit_loss_change.append(change)
    total_change = sum(profit_loss_change)
    monthly_change = total_change/len(profit_loss_change) 
print(f"Monthly average change in Profit/Losses:{monthly_change}")

#find greatest increase in profits (month and amount)
greatest_increase = max(profit_loss_change)
y = profit_loss_change.index(greatest_increase)
increase_month = month[y+1]
print(f"Greatest Increase in Profits: Month - {increase_month}, Amount - {greatest_increase}")

#find greatest decrease in profits ( month and amount)
greatest_decrease = min(profit_loss_change)
y = profit_loss_change.index(greatest_decrease)
decrease_month = month[y+1]
print(f"Greatest Decrease in Profits: Month - {decrease_month}, Amount - {greatest_decrease}")

#writing new file
final_script = os.path.join('Analysis', 'Pybank_results.csv')

#opening new file and writing text output
with open(final_script, 'w') as csvfile:
    csvfile.write("Financial Analysis\n")
    csvfile.write("-----------------------\n")
    csvfile.write(f"Total Months:{len(month)}\n")
    csvfile.write(f"Net Total Profit/Losses:${net_total:,}\n")
    csvfile.write(f"Monthly average change in Profit/Losses:${monthly_change:,.2f}\n")
    csvfile.write(f"Greatest Increase in Profits: Month - {increase_month}, Amount - ${greatest_increase:,}\n")
    csvfile.write(f"Greatest Decrease in Profits: Month - {decrease_month}, Amount - ${greatest_decrease:,}\n")

