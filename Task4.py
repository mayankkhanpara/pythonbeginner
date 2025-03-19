import math

def cal_squ_root():
    num= int(input("enter your number:"))
    return math.sqrt(num)

def round_number():
    num= float(input("enter your round number:"))
    return math.floor(num), math.ceil(num)

square_root= cal_squ_root()
floor_value, ceil_value = round_number()

print(f"The square root is: {square_root}")
print(f"The floor value is: {floor_value}, and the ceil vale is: {ceil_value}")

