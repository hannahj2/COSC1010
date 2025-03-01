#
# Hannah Johnson
# 02/28/2025
# Budget Analysis Programming Project
# COSC 1010
#
# Use comments liberally throughout the program.
# Variables
budget = 0
continueExpense = 'y' # yes or no to continue to add expenses
total = 0
overBudget = 0
underBudget = 0

# Ask user to enter amount they have budgeted for a month
budget = float(input('How much is your budget for the month?: $'))

# Prompt the user to enter each of their expenses
while continueExpense == 'y':
    expense = float(input('Enter an expense: $'))

    # Adds up the expenses
    total += expense

    # Ask the user again if they have an expense
    continueExpense = (input('Do you have more expenses to add? (y or n): '))

# Check to see if user is over or under budget
if total > budget:

    # Sees how much they are over budget
    overBudget = total - budget
    
    # Print how over budget they are
    print(f'You were over your budget by ${overBudget:.2f}. Try spending less!' )
elif total < budget:

    # Sees how much they are under budget
    underBudget = budget - total

    # Print how under budget they are
    print(f'You were under your budget by ${underBudget:.2f}. Nice job!')

    # Print that they used all their budget
    # If not under or over budget
else:
    print('You used all of your budget!')   
