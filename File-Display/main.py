#
# Hannah Johnson
# 04/03/2025
# File Display Programming Project
# COSC 1010
#
# Use comments liberally throughout the program.

# Open the file named numbers.txt
def main():
    numberFile = open('numbers.txt', 'r')

    # Read the file's contents
    for line in numberFile:
        number = int(line)

        # Display the file's contents
        print(number)

    # Close the file
    numberFile.close()

# Execute main() function
if __name__ == '__main__':
    main()