# Problem Statement: Write a Python program that takes the length and width of a rectangle as input from the user and prints both its area and perimeter.

# Take length input from the user and convert it to a float
length = float(input("Enter the length of the rectangle: "))

# Take width input from the user and convert it to a float
width = float(input("Enter the width of the rectangle: "))

# Calculate the area of the rectangle
area = length * width

# Calculate the perimeter of the rectangle
perimeter = 2 * (length + width)

# Print the area
print("The area of the rectangle is:", area)

# Print the perimeter
print("The perimeter of the rectangle is:", perimeter)
