def print_numbers():
    for i in range(1, 11):
        print(i)
print_numbers()

def print_even_numbers():
    for i in range(2, 11, 2):
        print(i)
print_even_numbers()

def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
num = int(input("Enter a number for multiplication table: "))
print(f"Multiplication table of {num}:")
multiplication_table(num)