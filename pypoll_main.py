import os
import csv

# Set path for file
# Machine agnostic script csvpath = os.path.join("..", "Resources", "election_data.csv")
csvpath = 'C:/Users/Omar/Documents/GitHub/python-challenge/PyPoll/Resources/election_data.csv'
print (csvpath)

# Read in the CSV file
with open(csvpath, newline='') as csvfile:

    # Split the data on commas, and read the file
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip the header line
    header = next(csvreader)
    
    # Name a list of values for the profit / losses to be later referenced
    voterid=[]
    county=[]
    candidate=[]

    
    # Create a list of the profitloss values
    for row in csvreader:
        voterid.append(int(row[0]))
        county.append(str(row[1]))
        candidate.append(str(row[2]))
        
        
        # Find the total number of votes cast
        count_votes = sum(1 for row in csvreader)
        #**Print to check that it works
        print(f'{count_votes}')

    # Find a complete list of the candidates who received votes
    def unique(candidate): 
  
        # intilize a null list 
        unique_list = [""] 
      
        # traverse for all elements 
        for x in candidate: 
            # check if exists in unique_list or not 
            if x not in unique_list: 
                unique_list.append(x) 
        # print list 
        for x in unique_list: 
            print(x)
            print(unique_list)

    # The percentage of votes each candidate won, by finding the total votes that each candidate won, then dividing by the total vote count
    # Note - this is not working, and I was not able to debug/fix in time before submission (I have set up time to review with tutor in session)
    khan_count = 0
    correy_count = 0
    li_count = 0
    otooley_count = 0

    for x in candidate:
        if x == 'Khan':
            khan_count = khan_count + 1
        elif x == 'Correy':
            correy_count = correy_count + 1
        elif x == 'Li':
            li_count = li_count + 1
        else:
            otooley_count = otooley_count + 1

    print(khan_count)
    print(correy_count)
    print(li_count)
    print(otooley_count)
     
    # The winner of the election based on popular vote
    # Note - was not able to find, because the calcs were not working, as noted above (tutoring session scheduled)
    khan_percent = round((khan_count / count_votes),3)
    correy_percent = round((correy_count / count_votes),3)
    li_percent = round((li_count / count_votes),3)
    otooley_percent = round((otooley_count / count_votes),3)

# Print the results to a separate file
# Open the file using "write" mode. Specify the variable to hold the contents
# Machine agnostic script csvpath = os.path.join("..", "PyPoll", "poll_print.csv")
print_path = 'C:/Users/Omar/Documents/GitHub/python-challenge/PyPoll/poll_print.csv'
print (print_path)

with open(print_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow('Election Results')
    csvwriter.writerow('-------------------')
    csvwriter.writerow('Total Votes: {count_votes}')
    csvwriter.writerow('-------------------')
    csvwriter.writerow('Khan: {khan_count} {khan_percent}')
    csvwriter.writerow('Correy: {correy_count} {correy_percent}')
    csvwriter.writerow('Li: {li_count} {li_percent}')
    csvwriter.writerow('O Tooley: {otooley_count} {otooley_percent}')