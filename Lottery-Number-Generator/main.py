#
# Hannah Johnson
# 04/10/2025
# Lottery Number Generator Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

# Need to import random to use
import random

# Variables
MAX_NUMBERS = 7 # Amount of numbers to print
START_RANGE = 0 # Number for starting range
END_RANGE = 9 # Number for ending range

def main():
    # Create a list with 7 numbers
    numbers = [0] * 7 # Repeats 7 times [0, 0, 0, 0, 0, 0, 0]

    # Loop that generates random numbers
    for index in range(MAX_NUMBERS):
        numbers[index] = random.randint(START_RANGE, END_RANGE)
        
    print('Here are your lottery numbers:')
   
    # Loop that displays the contents of the list
    for index in range(MAX_NUMBERS):

        # Prints the list. end='' makes them all on one line
        print(numbers[index], end='')

    # Prints another empty line
    print()

# Call main function
main()