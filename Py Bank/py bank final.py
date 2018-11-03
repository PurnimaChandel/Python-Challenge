import os
import csv

csvpath = os.path.join('budget_data.csv')
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")
    header = next(csvreader)
    csvlist = list(csvreader)
    #dates= []
    revenues =[]
    rev_change =[]
    total_rev = 0
    
    
    for row in  csvlist:
        #dates.append(row[0])
        revenues.append(int(row[1]))
        
    #Calculate Total Months and Total net amount of "Profit/Losses" 
    for i in revenues:
        total_months = len(revenues)
        total_rev += int(i)
    
    #Calculate Change in Profit/Loss
    rev_change = [revenues[i+1] - revenues[i] for i in range(len(revenues) -1)]
    
    #Calculate Average change in "Profit/Losses" 
    total_rev_change = sum(rev_change)
    no_of_periods = len(rev_change)
    average_rev_change = total_rev_change/no_of_periods
   
    #Calculate Greatest Increase in Profits
    max_change = max(rev_change)
    max_month = None
    initial_profit = None

    for row in  csvlist:
       if initial_profit is None:
           initial_profit = int(row[1])
           continue
       if int(row[1]) - initial_profit == max_change:
           max_month = row[0]
       initial_profit = int(row[1])

#Calculate Greatest Decrease in Profits
    min_profit = min(rev_change)
    min_profit_month = None
    initial_loss = None
    for row in  csvlist:
       if initial_loss is None:
           initial_loss = int(row[1])
           continue
       if (int(row[1]) - initial_loss) == min_profit:
           min_profit_month = row[0]
       initial_loss = int(row[1])

#Final Output
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(total_months))
    print("Total: $" + str(total_rev))
    print("Average Change: $" + str(average_rev_change))
    print("Greatest Increase in Profits: " + str(max_month) +" $" + str(max_change))
    print("Greatest Decrease in Profits: " + str(min_profit_month) +" $" + str(min_profit))
    