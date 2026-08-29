# Take inputs from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform basic operations
print(f"Addition: {num1} + {num2} = {num1 + num2}")
print(f"Multiplication: {num1} x {num2} = {num1 * num2}")

# Use conditional logic for safety
if num2 != 0:
    print(f"Division: {num1} / {num2} = {num1 / num2}")
else:
    print("Division: Cannot divide by zero!")
