#
# Hannah Johnson
# 02/21/2025
# Hot Dog Cookout Calculator Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

# Constants
HOT_DOG_PACKAGES = 10
HOT_DOG_BUNS = 8

# Variables
numberOfPeople = 0      # number of people attending
numberPerPerson = 0     # hot dogs and buns each person will be given
total = 0               # number of hot dog packages and hot dog buns needed
minimumDogs = 0         # minimum number of packages of hot dogs required
minimumBuns = 0         # minimum number of packages of hot dog buns required
hotDogsLeftOver = 0     # hot dogs that will be left over
hotDogBunsLeftOver = 0  # hot dog buns that will be left over


# Get the number of people attending
# Needs to be int() since we're working with numbers
# Needs to be an input so we can get the keyboard input
numberOfPeople = int(input("Enter the number of people attending: "))

# Get the number of hot dogs each person will be given
# Needs to be int() since we're working with numbers
# Needs to be an input so we can get the keyboard input
numberPerPerson = int(input("Enter the number of hot dogs each person will be given: "))

# Calculate the number of hot dog packages and hot dog buns needed
total = numberOfPeople * numberPerPerson

# Calculate the minimum number of packages of hot dogs required
# Assigning minimumDogs equal to 
# total of hot dogs and buns divided by hot dog packages
# Floor division (//) rounds down
# Ex: 8 people * 2 hot dogs each person = 16 (total HDs) // 10 (HD packet) = 1 remainder 6
minimumDogs = total // HOT_DOG_PACKAGES

# See if the number of people attending is large enough to need more than one package of hot dogs
if minimumDogs > 0:
    # Calculate the number of hot dogs that will be left over from a package
    # Modulus (%) is remainder
    # Ex: 8 people * 2 hot dogs each person = 16 (total HDs) % 10 (HD packet) = remainder 6
    hotDogsLeftOver = total % HOT_DOG_PACKAGES

    # If leftovers, add another package of hot dogs
    # Ex: 16 total HDs % 10 = remainder 6 (need another package since it's != 0)
    if hotDogsLeftOver != 0:
        minimumDogs += 1 # Adding 1 to the variable (or minimumDogs = minimumDogs + 1)

    # Set minimum number of hot dog packages to 1 because the people attending is small enough to only need 1 package of hot dogs
else:
    minimumDogs = 1

# Calculate the number of hot dogs that will be left over
hotDogsLeftOver = HOT_DOG_PACKAGES * minimumDogs - total

# Calculate the minimum number of packages of hot dog buns required
# Assigning minimumBuns equal to 
# total of hot dogs and buns divided by hot dog buns
# Floor division (//) rounds down
minimumBuns = total // HOT_DOG_BUNS

# See if the number of people attending is large enough to need more than one package of hot dog buns
if minimumBuns > 0:
    # Calculate the number of hot dogs that will be left over from a package
    # Modulus (%) is remainder
    hotDogBunsLeftOver = total % HOT_DOG_BUNS

    # If leftovers, add another package of hot dog buns
    if hotDogBunsLeftOver != 0:
        minimumBuns += 1 # Adding 1 to the variable (or minimumBuns = minimumBuns + 1)

    # Set minimum number of hot dog buns to 1 because the people attending is small enough to only need 1 package of hot dogs
else:
    minimumBuns = 1

# Calculate the number of hot dog buns that will be left over
hotDogBunsLeftOver = HOT_DOG_BUNS * minimumBuns - total

# Display the minimum number of packages of hot dogs required
print("Minimum packages of hot dogs required: ", minimumDogs)

# Display the minimum number of packages of hot dog buns required
print("Minimum packages of hot dog buns required: ", minimumBuns)

# Display the number of hot dogs that will be left over
print("Leftover hot dogs: ", hotDogsLeftOver)

# Display the number of hot dog buns that will be left over
print("Leftover hot dog buns: ", hotDogBunsLeftOver)
