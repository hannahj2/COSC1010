#
# Hannah Johnson
# 02/12/2025
# Sales Prediction Programming Project
# COSC 1010
#

# Variables to hold the sales total and the profit
# totalSales
# profit

# Get the amount of projected sales.
totalSales = float(input('Enter the projected sales: ')) # Reads the input

# Calculate the projected profit.
profit = totalSales * 0.23 # totalSales * 0.23 (23%)

# Print the projected profit.
print('The profit is $', format(profit, ',.2f'))