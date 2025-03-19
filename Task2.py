def greet_user():
    name = input("Enter your name: ")
    print(f"Hello, {name}! Welcome!")

def add_numbers():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    return num1 + num2

# Call functions
greet_user()
sum_result = add_numbers()

# Display result
print(f"The sum of the two numbers is: {sum_result}")