# Problem Statement: Write a Python program that takes two numbers as input from the user and prints their addition, subtraction, multiplication, and division.

# Source Code (python) ------------------------

# Take the first number as input and convert it to a float
num1 = float(input("Enter the first number: "))

# Take the second number as input and convert it to a float
num2 = float(input("Enter the second number: "))

# Perform addition
addition = num1 + num2

# Perform subtraction
subtraction = num1 - num2

# Perform multiplication
multiplication = num1 * num2

# Perform division (handle division by zero)
if num2 != 0:
    division = num1 / num2
else:
    division = "Undefined (division by zero)"

# Print results
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
