# Problem Statement : Take two integers and swap them using a third variable and with using a third variable.

# Source Code (python) ------------------------

num1 = int(input("Enter the value of num1 : "))
num2 = int(input("Enter the value of num2 : "))

# Swap with a third variable
temp = num1
num1 = num2
num2 = temp

print(f"After swapping using third variable :\nnum1 : {num1}\nnum2 : {num2}")

# Swap without a third variable
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print(f"After swapping Without third variable :\nnum1 : {num1}\nnum2 : {num2}")
