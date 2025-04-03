#
# Hannah Johnson
# 04/03/2025
# File Display Programming Project
# COSC 1010
#
# Use comments liberally throughout the program.

# Open the file named numbers.txt
def main():
    number_file = open('./File-Display/numbers.txt', 'r')

    # Read the file's contents
    file_contents = number_file.read()

    # Display the file's contents
    print(file_contents)

    # Close the file
    number_file.close()

if __name__ == '__main__':
    main()