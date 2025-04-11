#
# Hannah Johnson
# 04/10/2025
# Magic 8 Ball Programming Project
# COSC 1010
#
# Use comments liberally throughout the program.

# Import random to use choice()
import random

# Open the file named 8_ball_responses.txt in read mode ('r')
def main():
    eightBallFile = open('8_ball_responses.txt', 'r')

    # Create an empty list
    responses = []

    # Read the responses from the file
    for line in eightBallFile:
        responses.append(line)

    # Close the file
    eightBallFile.close()

    # Have to put question in a while loop or "break" won't work
    while True:
        # Prompt the user to ask a question or type quit to exit
        question = input('Ask a question (or type quit to exit): ')

        # If user types "quit", end the loop
        if question == "quit":
            print('Thanks for playing Magic 8 Ball!')
            break # gives error if not in while loop

        # Display one of the responses randomly
        randomResponse = random.choice(responses)

        # Prints the response
        print(f'The Magic 8 Ball says: {randomResponse}')

# Execute main() function
if __name__ == '__main__':
    main()