#
# Hannah Johnson
# 02/12/2025
# Sales Tax Programming Project
# COSC 2409 DNT
#

# Variable declarations
purchase = 0.0
stateSalesTax = 0.0
countySalesTax = 0.0
totalSalesTax = 0.0
totalSale = 0.0

# Constants for the state and county tax rates
# Constants are usually in all caps
STATE_TAX = 0.05 
COUNTY_TAX = 0.025

# Get the amount of the purchase.
# Set a variable to enter the amount of the purchase
# Use input to grab input of computer
# Add space after input message or the message will be messy
# Will automatically be a string
# So set it as a float since we're working with numbers
purchaseAmount = float(input('Enter the amount of the purchase: '))

# Calculate the state sales tax.
# State tax is the purchase amount * the state tax
stateTax = purchaseAmount * STATE_TAX

# Calculate the county sales tax.
# County tax is the purchase amount * the county tax
countyTax = purchaseAmount * COUNTY_TAX

# Calculate the total tax.
# To get the total, add the stateTax & countyTax together
totalTax = stateTax + countyTax

# Calculate the total of the sale.
# Total sale is the purchase amount + the total tax
totalSale = purchaseAmount + totalTax

# Print information about the sale.
print("Purchase Amount:", format(purchaseAmount, '.2f'))
print("State Tax:", format(stateTax, '.2f'))
print("County Tax:", format(countyTax, '.2f'))
print("Total Tax:", format(totalTax, '.2f'))
print("Sales Total:", format(totalSale, '.2f'))