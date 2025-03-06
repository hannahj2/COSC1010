#
# Hannah Johnson
# 03/05/2025
# Kilometer Converter Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

# Variables
distanceInKilo = 0
distanceInMiles = 0
CONVERSION_FORMULA = 0.6214 # Use a constant to hold this number

# Asks the user to enter a distance in kilometers
def main():
    distanceInKilo = float(input('Enter a distance in kilometers: '))

    # Call distanceToMiles function to display distance to miles
    distanceToMiles(distanceInKilo)

# Convert distance to miles
def distanceToMiles(kilometers):

    # Formula to convert km to miles
    distanceInMiles = kilometers * CONVERSION_FORMULA

    # Displays distance to miles
    # Only displays 2 decimal points
    print(f'{kilometers} kilometers equals {distanceInMiles: .3f} miles.')

# Call main function to start/execute the program
main()