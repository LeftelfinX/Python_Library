# Problem Statement : Take radius as input and print area & circumference of a circle.

# Source Code (python) ------------------------

pi = 3.14
radius = int(input("Enter the radius : "))

area = pi * (radius ** 2)
print("Area :",area)

circumference = 2 * pi * radius
print("Circumference :",circumference)

