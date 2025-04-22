#
# Name
# Date
# Capital Quiz Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

import random

# Number of states to quiz the user
NUMBER_OF_STATES = 5

def main():
    # Initialize dictionary
    capitals = {'Alabama':'Montgomery', 'Alaska':'Juneau',
                'Arizona':'Phoenix', 'Arkansas':'Little Rock',
                'California':'Sacramento', 'Colorado':'Denver',
                'Connecticut':'Hartford', 'Delaware':'Dover',
                'Florida':'Tallahassee', 'Georgia':'Atlanta',
                'Hawaii':'Honolulu', 'Idaho':'Boise',
                'Illinois':'Springfield', 'Indiana':'Indianapolis',
                'Iowa':'Des Moines', 'Kansas':'Topeka',
                'Kentucky':'Frankfort', 'Louisiana':'Baton Rouge',
                'Maine':'Augusta', 'Maryland':'Annapolis',
                'Massachusetts':'Boston', 'Michigan':'Lansing',
                'Minnesota':'Saint Paul', 'Mississippi':'Jackson',
                'Missouri':'Jefferson City', 'Montana':'Helena',
                'Nebraska':'Lincoln', 'Nevada':'Carson City',
                'New Hampshire':'Concord', 'New Jersey':'Trenton',
                'New Mexico':'Santa Fe', 'New York':'Albany',
                'North Carolina':'Raleigh', 'North Dakota':'Bismarck',
                'Ohio':'Columbus', 'Oklahoma':'Oklahoma City',
                'Oregon':'Salem', 'Pennsylvania':'Harrisburg',
                'Rhode Island':'Providence', 'South Carolina':'Columbia',
                'South Dakota':'Pierre', 'Tennessee':'Nashville',
                'Texas':'Austin', 'Utah':'Salt Lake City',
                'Vermont':'Montpelier', 'Virginia':'Richmond',
                'Washington':'Olympia', 'West Virginia':'Charleston',
                'Wisconsin':'Madison', 'Wyoming':'Cheyenne'}
    while True:
        # Local variables
        correct = 0 # Keeps count of correct responses
        incorrect = 0 # Keeps count of incorrect responses

        # Quiz the user
        for count in range(NUMBER_OF_STATES):
            
            # At first, I did = capitals.popitem()
            # but it only returned the last 5 states

            # Get a random state & capital
            state, capital = random.choice(list(capitals.items()))

            # User input to ask user for the capital
            quiz = input(f'What is the capital of {state}? ')

            # If user response is correct
            if quiz.lower() == capital.lower():

                # Add 1 to correct responses
                correct += 1

                # Print message showing the user they got it correct
                print('Great job! You got this correct!')

            # If user response is incorrect
            else:

                # Add 1 to incorrect responses
                incorrect += 1

                # Print message showing the user they got it incorrect
                print(f'Incorrect! The capital of {state} is {capital}.')

        # Display the correct and incorrect responses
        print('\nHere are your results: ')
        print(f'Correct responses: {correct}')
        print(f'Incorrect responses: {incorrect}')

        # Continue until user quits the game.
        continueGame = input('\nWould you like to continue? (y for yes, n for no): ')

        if continueGame.lower() != 'y':
            print('Thanks for playing the capital quiz! Bye!')
            break
# Call the main function.
main()
