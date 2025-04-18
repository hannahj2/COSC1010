#
# Hannah Johnson
# 04/17/2025
# Vowels and Consonants Programming Project
# COSC 1010
#
# Use comments liberally throughout the program.

# User input for entering a string
def main():
    stringInput = input('Enter a sentence: ')

    # Displays the number of vowels and consonants the string contains
    print(f'This string has {numberOfVowels(stringInput)} vowels and {numberOfConsonants(stringInput)} consonants.')

    # (Another step could maybe be ending the program after user input?)

# Function that accepts a string as an argument
def numberOfVowels(string):

    # List of vowels
    vowelList = ['a', 'e', 'i', 'o', 'u']

    # Accumulator to count the number of vowels in a string
    vowelCount = 0

    # For loop to count vowels
    for v in string:
        # if it is in the list of vowels
        # lower() returns the lowercase version
        if v.lower() in vowelList:
            # Add 1 to accumulator
            vowelCount += 1

    # Returns the number of vowels the string contains
    return vowelCount

# Other function that accepts a string as an argument
def numberOfConsonants(string):

    # List of vowels
    vowelList = ['a', 'e', 'i', 'o', 'u']

    # Accumulator to count the number of consonants in a string
    consonantCount = 0
    
     # For loop to count consonants
    for c in string:
        # if it is a letter and NOT in the vowelList
        # isalpha() returns true if alphabetic letter
        # lower() returns the lowercase version
        if c.isalpha() and c.lower() not in vowelList:
            # Add 1 to accumulator
            consonantCount += 1

    # Returns the number of consonants the string contains
    return consonantCount
    
# Execute the main function
main()