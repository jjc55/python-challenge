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
greatest_decrease_date = str("")

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
    
    greatest_increase = max(changes_list)
    index_greatest_increase = changes_list.index(max(changes_list))
    greatest_increase_date = months_list[index_greatest_increase]
    
    greatest_decrease = min(changes_list) 
    index_greatest_decrease = changes_list.index(min(changes_list))
    greatest_decrease_date = months_list[index_greatest_decrease]    
    
    with open(os.path.join("PyBank-output-file.txt"), "w") as textfile:
        textfile.write("Financial Analysis")
        textfile.write(" \n") 
        textfile.write("--------------------------- \n")       
        textfile.write(f"Total Months: {months}\n")
        textfile.write(f"Total: ${net_total}\n")
        textfile.write(f"Average change: ${average_change:0.2f}\n")
        textfile.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
        textfile.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")
        