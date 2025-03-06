#
# Hannah Johnson
# 03/05/2025
# Feet to Inches Programming Project
# COSC 1010
#
# Use comments liberally throughout the program.
numOfFeet = 0
numOfInches = 0
CONVERSION_FORMULA = 12

# Prompt user to enter the number of feet
def main():
    numOfFeet = int(input('Enter the number of feet: '))

# Call feet_to_inches to display number of inches in feet
    feet_to_inches(numOfFeet)

# Write function called feet_to_inches
def feet_to_inches(feet): # Accepts feet as argument

    # Formula to convert feet to inches
    numOfInches = feet * CONVERSION_FORMULA

    # Check to see if feet == 1.0
    if feet == 1:
        # If so, print "foot" instead of "feet"
        print(f'{feet} foot equals {numOfInches} inches.')
    else: 
         # Else, print "feet"
        print(f'{feet} feet equals {numOfInches} inches.')

# Call main function to start program
main()