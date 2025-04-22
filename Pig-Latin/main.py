#
# Hannah Johnson
# 04/17/2025
# Pig Latin Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

# User input for entering a sentence
def pigLatinConverter():

    sentence = input('Enter a sentence: ').split()
    
    # For loop
    for word in sentence:
        
        # Uses the length of the string as the end if you leave out end
        # Remove 1st letter
        removeFirstLetter = word[1:]

        # Python uses 0 if you leave out start index
        # Adds letter to the end
        addLetterEnd = word[:1]

        # Adds 'ay' to the end
        pigLatin = 'ay'
        
        # end=' ' makes it so all the words are on one line
        print(removeFirstLetter + addLetterEnd + pigLatin, end=' ')

pigLatinConverter()