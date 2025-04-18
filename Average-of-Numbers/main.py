#
# Hannah Johnson
# 04/03/2025
# Average of Numbers Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 


# Open the file named numbers.txt
def main():
    # Variables
    total = 0
    lines = 0
    numberFile = open('numbers.txt', 'r')

    # Reads the first line
    # When finished, it will go to the next line
    fileContents = numberFile.readline()

    # Check to see if fileContents is empty string
    while fileContents != "":

        # Convert to integer
        number = int(fileContents)

        # Increase total and lines
        total += number # or total = total + number
        lines += 1 # or lines = lines + 1

        # Read the next line (infinite loop if this isn't here)
        fileContents = numberFile.readline()

    # Calculates average of numbers
    average = total / lines

    # Displays the average
    print("The average is:", average)

# Execute main() function
if __name__ == '__main__':
    main()