#
# Hannah Johnson
# 02/28/2025
# Bug Collector Programming Project
# COSC 1010
#
# Initialize variables for bugs and total number of bugs collected.
totalBugs = 0 # total number of bugs
bugs = 0

# Get number of bugs collected each day using a for loop.
for day in range(1, 8): # will print 1-7

    # Asking user to input the number of bugs collected
    bugs = int(input(f'Enter the bugs collected on day {day}: '))
    
    # Accumulator adding bugs to totalBugs
    totalBugs += bugs # could also be totalBugs = totalBugs + bugs

# Display the total number of bugs collected.
print('You collected a total of', totalBugs, 'bugs.')