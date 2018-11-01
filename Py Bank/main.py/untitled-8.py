import os
import csv

csvpath = os.path.join('budget_data.csv')

def add_list (input_list):
    sum = 0
    for item in input_list:
        sum = sum + int(item)
    return sum

def row_count (input_list1):
    row_count = len(input_list1)
    return row_count

def change (input_list2):
    for i in input_list2:
        change = int(i+1)-int(i)

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")
    header = next(csvreader)

    profit_loss = []
    change =[]
   
    for row in csvreader:
        Profit_loss = row[1]
        profit_loss.append(Profit_loss)
       

    print(add_list(profit_loss))
    print(row_count(profit_loss))
    
    
    