import os
import csv

budget_data = os.path.join(".","Resources","budget_data.csv")

months = int(0)
net_total = int(0)
monthly_change = int(0)
changes_list = []
months_list = []
previous = int(0)
greatest_increase = int(0)
greatest_increase_date = str("")
greatest_decrease = int(0)

with open (budget_data, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)

    for index, row in enumerate(csvreader):
        # index = 0, row = ["jan - 10", "1088983"]
        # index = 1, row = ["feb - 10", "-354534"]
        # ETC.
        months = months + 1
        net_total = net_total + int(row[1])
        if index > 0:
            monthly_change = int(row[1]) - previous
            changes_list.append(monthly_change)
            months_list.append(row[0])
        previous = int(row[1])
            
    average_change = sum(changes_list)/len(changes_list)      
        #append the monthly change=next row profit/loss - the current row's loss and the date 
        #add to monthly_change dictionary {change:date} or 2 separate lists}
        #iterate through and find the greatest increase and greatest decrease
           
    print(f"Total Months: {months}")
    print(f"Total: ${net_total}")
    print(f"Average change: ${average_change:0.2f}")
    print(f"Greatest Increase in Profits:()")
    print(f"Greatest Decrease in Profits:()")
    
    
    