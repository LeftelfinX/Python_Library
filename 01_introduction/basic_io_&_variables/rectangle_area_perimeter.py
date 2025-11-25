# Problem Statement: Write a Python program that takes the length and width of a rectangle as input from the user and prints both its area and perimeter.

# Source Code (python) ------------------------

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = length * width
print("The area of the rectangle is:", area)

perimeter = 2 * (length + width)
print("The perimeter of the rectangle is:", perimeter)
