import csv
import os

# CSV path
budget_data_csv = os.path.join("/Users/mackenzieswaney/pybank/", 'budget_data.csv')

# Total months output/ tracking
total_months = 0

# Create lists
months = []
net = []
changes = []

# Read CSV
with open(budget_data_csv, newline='') as csvfile:
    bankreader = csv.reader(csvfile, delimiter=",")

    # Read header row
    csv_header = next(csvfile)

# Loop through CSV - count months & total rev
    for row in bankreader:
        total_months = total_months + 1
        net.append(int(row[1]))
        prev = total_months - 1
        change = int(row[1]) - net[(prev-1)]
        changes.append(change)
        months.append(str(row[0]))
       
# Define variables
total = sum(net)
average_change = round(sum(changes)/(len(changes)-1), 2)
max_val = max(changes)
min_val = min(changes)
max_ind = changes.index(max_val)
min_ind = changes.index(min_val)
max_month = months[max_ind]
min_month = months[min_ind]

# Print to terminal
print("Financial Analysis")
print("-------------------------")
print(f'Total Months: {total_months}')
print(f'Total: ${total}')
print(f'Average Change: #{average_change}')
print(f'Greatest Increase in Profits: {max_month} (${max_val})')
print(f'Greatest Decrease in Profits: {min_month} (${min_val})')

# Print to txt file
textfile = open("pybankmackenzie.txt", "w")

textfile.write("Financial Analysis\n")
textfile.write("-------------------------\n")
textfile.write(f'Total Months: {total_months}\n')
textfile.write(f'Total: ${total}\n')
textfile.write(f'Average Change: ${average_change}\n')
textfile.write(f'Greatest Increase in Profits: {max_month} (${max_val})\n')
textfile.write(f'Greatest Decrease in Profits: {min_month} (${min_val})')