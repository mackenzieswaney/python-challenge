# Import
import os
import csv

election_data_csv = os.path.join("/Users/mackenzieswaney/pypoll/", "election_data.csv")

# Create dicionary
election = {}

# Count votes
votes_count = 0

# Read CSV file & Initialize Variables
with open(election_data_csv, newline='') as csvfile:
    pollreader = csv.reader(csvfile, delimiter=',')

    # Read header row
    csv_header = next(csvfile)

# Loop through CSV - count votes per candidate & total votes
    for row in pollreader:
        votes_count = votes_count + 1
        if row[2] in election.keys():
            election[row[2]] = election[row[2]] + 1
        else:
            election[row[2]] = 1

# Candidate & vote list
candidate = []
num_votes = []

# Append dictionary to list of candidate name & vote count
for key, value in election.items():
    candidate.append(key)
    num_votes.append(value)

# Percent won/ list
percent = []
for i in num_votes:
    percent.append(round((i)/(votes_count)*100, 1))

# Clean data
results = list(zip(candidate, num_votes, percent))

# Winner List
winner_list = []

for item in results:
    if max(num_votes) == item[1]:
        winner_list.append(item[0])

# Winner list to winner name
winner = winner_list[0]

# Print to terminal
print(f'\nElection Results \n------------------------- \nTotal Votes: ' +str(votes_count) + '\n-------------------------')
for item in results:
    print(item[0] + f': ' + str(item[2]) +'% (' + str(item[1]) + ')')
print(f'------------------------- \nWinner: '+ winner +'\n-------------------------')

# Print txtfile
textfile = open("pypollmackenzie.txt", "w")

textfile.write("Election Results\n")
textfile.write(f'-------------------------\n')
textfile.write(f'Total Votes: ' +str(votes_count) + '\n')
textfile.write(f'-------------------------\n')
for item in results:
    textfile.write(item[0] + f': ' + str(item[2]) +'% (' + str(item[1]) + ')\n')
textfile.write(f'-------------------------\n')
textfile.write(f'Winner: ' + winner + '\n')
textfile.write(f'-------------------------') 