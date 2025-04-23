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

    encryptedCodes = {
        'A':')','a':'0','B':'(','b':'9','C':'*','c':'8',\
        'D':'&','d':'7','E':'^','e':'6','F':'%','f':'5',\
        'G':'$','g':'4','H':'#','h':'3','I':'@','i':'2',\
        'J':'!','j':'1','K':'Z','k':'z','L':'Y','l':'y',\
        'M':'X','m':'x','N':'W','n':'w','O':'V','o':'v',\
        'P':'U','p':'u','Q':'T','q':'t','R':'S','r':'s',\
        'S':'R','s':'r','T':'Q','t':'q','U':'P','u':'p',\
        'V':'O','v':'o','W':'N','w':'n','X':'M','x':'m',\
        'Y':'L','y':'l','Z':'K','z':'k','!':'J','1':'j',\
        '@':'I','2':'i','#':'H','3':'h','$':'G','4':'g',\
        '%':'F','5':'f','^':'E','6':'e','&':'D','7':'d',\
        '*':'C','8':'c','(':'B','9':'b',')':'A','0':'a',\
        ':':',',',':':','?':'.','.':'?','<':'>','>':'<',\
        "'":'"','"':"'",'+':'-','-':'+','=':';',';':'=',\
        '{':'[','[':'{','}':']',']':'}'
        }
    
    # Open the file named text.txt
    with open(TEXT_FILE, 'r') as readTextFile:

        # Read the file's contents
        textFileContents = readTextFile.read()

        # Use the dictionary 
        # to write an encrypted version of the file's contents
        encryptedContents = ''
        for character in textFileContents:
            if character in encryptedCodes:

                # replace letter with coded
                encryptedContents += encryptedCodes[character]
            else:
                # not alphabetic characters stay the same
                encryptedContents += character

        with open(ENCRYPTED_FILE, 'w') as writeTextFile:
            writeTextFile.write(encryptedContents)

def decryptFile():

    # Codes
    decryptedCodes = {
        'A':')','a':'0','B':'(','b':'9','C':'*','c':'8',\
        'D':'&','d':'7','E':'^','e':'6','F':'%','f':'5',\
        'G':'$','g':'4','H':'#','h':'3','I':'@','i':'2',\
        'J':'!','j':'1','K':'Z','k':'z','L':'Y','l':'y',\
        'M':'X','m':'x','N':'W','n':'w','O':'V','o':'v',\
        'P':'U','p':'u','Q':'T','q':'t','R':'S','r':'s',\
        'S':'R','s':'r','T':'Q','t':'q','U':'P','u':'p',\
        'V':'O','v':'o','W':'N','w':'n','X':'M','x':'m',\
        'Y':'L','y':'l','Z':'K','z':'k','!':'J','1':'j',\
        '@':'I','2':'i','#':'H','3':'h','$':'G','4':'g',\
        '%':'F','5':'f','^':'E','6':'e','&':'D','7':'d',\
        '*':'C','8':'c','(':'B','9':'b',')':'A','0':'a',\
        ':':',',',':':','?':'.','.':'?','<':'>','>':'<',\
        "'":'"','"':"'",'+':'-','-':'+','=':';',';':'=',\
        '{':'[','[':'{','}':']',']':'}'
        }

    # Open the file named encrypted .txt
    with open(ENCRYPTED_FILE, 'r') as encryptedFile:

        # Read the file's contents
        encryptedFileContents = encryptedFile.read()

        # Decrypt the contents
        decryptedContents = ''
        for character in encryptedFileContents:
            if character in decryptedCodes:

                # replace letter with coded
                decryptedContents += decryptedCodes[character]
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