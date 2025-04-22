#
# Hannah Johnson
# 04/21/2025
# File Encryption and Decryption Programming Project
# COSC 1010
#
# Use comments liberally throughout the program.

# Constants
TEXT_FILE = 'text.txt'
ENCRYPTED_FILE = 'encrypted.txt'

def encryptFile():

    codes = {
        'A': '%', 'a': '9', 'B': '@', 'b': '#',
        'C': '!', 'c': '&', 'D': '$', 'd': '1',
        'E': '*', 'e': '0', 'F': '^', 'f': '3',
        'G': '+', 'g': '2', 'H': '~', 'h': '/',
        'I': '(', 'i': ')', 'J': '-', 'j': '=',
        'K': '{', 'k': '}', 'L': '[', 'l': ']',
        'M': ';', 'm': ':', 'N': '<', 'n': '>',
        'O': ',', 'o': '.', 'P': '|', 'p': '`',
        'Q': 'a', 'q': 'b', 'R': 'c', 'r': 'd',
        'S': 'e', 's': 'f', 'T': 'g', 't': 'h',
        'U': 'i', 'u': 'j', 'V': 'k', 'v': 'l',
        'W': 'm', 'w': 'n', 'X': 'o', 'x': 'p',
        'Y': 'q', 'y': 'r', 'Z': 's', 'z': 't'
        }
    
    # Open the file named text.txt
    with open(TEXT_FILE, 'r') as readTextFile:

        # Read the file's contents
        textFileContents = readTextFile.read()

        # Use the dictionary 
        # to write an encrypted version of the file's contents
        encryptedContents = ''
        for character in textFileContents:
            if character in codes:

                # replace letter with coded
                encryptedContents += codes[character]
            else:
                # not alphabetic characters stay the same
                encryptedContents += character

        with open(ENCRYPTED_FILE, 'w') as writeTextFile:
            writeTextFile.write(encryptedContents)

def decryptFile():

    # Reversed codes
    reversedCodes = {
        '%': 'A', '9': 'a', '@': 'B', '#': 'b',
        '!': 'C', '&': 'c', '$': 'D', '1': 'd',
        '*': 'E', '0': 'e', '^': 'F', '3': 'f',
        '+': 'G', '2': 'g', '~': 'H', '/': 'h',
        '(': 'I', ')': 'i', '-': 'J', '=': 'j',
        '{': 'K', '}': 'k', '[': 'L', ']': 'l',
        ';': 'M', ':': 'm', '<': 'N', '>': 'n',
        ',': 'O', '.': 'o', '|': 'P', '`': 'p',
        'a': 'Q', 'b': 'q', 'c': 'R', 'd': 'r',
        'e': 'S', 'f': 's', 'g': 'T', 'h': 't',
        'i': 'U', 'j': 'u', 'k': 'V', 'l': 'v',
        'm': 'W', 'n': 'w', 'o': 'X', 'p': 'x',
        'q': 'Y', 'r': 'y', 's': 'Z', 't': 'z'
        }

    # Open the file named encrypted .txt
    with open(ENCRYPTED_FILE, 'r') as encryptedFile:

        # Read the file's contents
        encryptedFileContents = encryptedFile.read()

        # Decrypt the contents
        decryptedContents = ''
        for character in encryptedFileContents:
            if character in reversedCodes:

                # replace letter with coded
                decryptedContents += reversedCodes[character]
            else:
                # not alphabetic characters stay the same
                decryptedContents += character

        # Displays the decrypted contents on the screen
        print('\nDecrypted contents: ')
        print(decryptedContents)

# Execute the encryptFile() function
encryptFile()
# Execute the decryptFile() function
decryptFile()