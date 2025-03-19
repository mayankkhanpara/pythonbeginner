# 1. Simple Calculations with Functions
def add_numbers(a, b):
    return a + b

def multiply_numbers(a, b):
    return a * b

# User input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Perform calculations
sum_result = add_numbers(num1, num2)
product_result = multiply_numbers(num1, num2)

# Print results
print(f"The sum of {num1} and {num2} is: {sum_result}")
print(f"The product of {num1} and {num2} is: {product_result}")