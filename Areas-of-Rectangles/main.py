#
# Hannah Johnson
# 02/21/2025
# Areas of Rectangles Programming Project
# COSC 1010
#
# Local variables
lengthA = 0
widthA = 0
lengthB = 0
widthB = 0
areaA = 0
areaB = 0

# Get length A
lengthA = int(input("Enter the length of rectangle A: "))

# Get width A
widthA = int(input("Enter the width of rectangle A: "))

# Get length B
lengthB = int(input("Enter the length of rectangle B: "))

# Get width B
widthB = int(input("Enter the width of rectangle B: "))

# Calculate area A
areaA = lengthA * widthA

# Calculate area B
areaB = lengthB * widthB

# Print area comparison using if-elif-else statements
if areaA > areaB:
    print("Rectangle A has the greater area.")
elif areaB > areaA:
    print("Rectangle B has the greater area.")
else:
    print("Both rectangles have the same area.")