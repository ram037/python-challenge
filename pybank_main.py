import os
import csv

# Set path for file

# Machine agnostic script csvpath = os.path.join("..", "Resources", "budget_data.csv")
csvpath = 'C:/Users/Omar/Documents/GitHub/python-challenge/PyBank/Resources/budget_data.csv'
print (csvpath)

# Read in the CSV file
with open(csvpath, newline='') as csvfile:
    
    # Split the data on commas, and read the file
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip the header line
    header = next(csvreader)
    
    # Name a list of values for the profit / losses to be later referenced
    months=[]
    profitlosses=[]
    changeprofitloss=[]

    # Create a list of the profitloss values


    for row in csvreader:
        months.append(str(row[0]))
        profitlosses.append(int(row[1]))
    
    #**Check to make sure the profitloss values are there
    #print(profitloss)

        # Using the profitloss values, find the monthly changes
        changeprofitloss=[profitlosses[i+1]-profitlosses[i] for i in range(len(profitlosses)-1)]

    #**Check to make sure calc is performed correctly
    #print(changeprofitloss)

    #Find the max and min
    max_change = (max(changeprofitloss))
    min_change = (min(changeprofitloss))
    max_increase = round(max(changeprofitloss),2)
    min_increase = round(min(changeprofitloss),2)

    # Find the specific information requested for the assignment
    months_count = (len(months)-1)
    total_profitloss = round(sum(profitlosses),2)
    averagechange = round(sum(changeprofitloss)/(months_count),2)

    # Find the corresponding dates for max_increase
    #?Having a difficult time finding the corresponding date and printing the corresponding date; below is my failed attempt 
    #bank_dict = {"months": months, "profitloss": profitlosses, "changeprofitloss": changeprofitloss}
    #print(bank_dict)
    #x = bank_dict["months"]
    #y = bank_dict["profitloss"]
    #z = bank_dict["changeprofitloss"]

    #for max_change in bank_dict["changeprofitloss"]:
    # print(bank_dict(x))
    #for x, z in bank_dict.items():
    # if z == max_change:

    # print(x)


# Print out the requested information
print(f'Financial Analysis')
print(f'--------------------------------------------')
print(f'Total Months: {months_count}')
print(f'Total Profit/Loss: ${total_profitloss}')
print(f'Average Change: ${averagechange}')
print(f'Greatest Increase in Profits: ${max_increase}')
print(f'Greatest Decrease in Profits: ${min_increase}')

#Write to file; first, specify the file to write to
output_path = os.path.join("..", "output", "new.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
# Machine agnostic script csvpath = os.path.join("..", "PyBank", "bank_print.csv")
print_path = 'C:/Users/Omar/Documents/GitHub/python-challenge/PyBank/bank_print.csv'
print (print_path)

with open(print_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow('Financial Analysis')
    csvwriter.writerow('--------------------------------------------')
    csvwriter.writerow('Total Months: {months_count}')
    csvwriter.writerow('Total Profit/Loss: ${total_profitloss}')
    csvwriter.writerow('Average Change: ${averagechange}')
    csvwriter.writerow('Greatest Increase in Profits: ${max_increase}')
    csvwriter.writerow('Greatest Decrease in Profits: ${min_increase}')