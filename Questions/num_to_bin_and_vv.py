# Number to binary
# M-1
def num_to_binary(x):
    binary_num = bin(x)[2:]
    return binary_num

x = int(input("Enter a decimal number: "))
print("Binary (using built-in):", num_to_binary(x))

# M-2
def num_to_binary_loop(x):
    binary_number = ""
    while x > 0:
        remainder = str(x % 2)
        binary_number = remainder + binary_number
        x = x // 2
    return binary_number    

x = int(input("Enter a decimal number: "))
print("Binary (using loop):", num_to_binary_loop(x))

# Vice-Versa Part
# M-1
def bin_to_dec(x):
    return int(x, 2)  # int(s, base) works for string

x = str(input("Enter a binary number: "))
print("Decimal (using built-in):", bin_to_dec(x))

# M-2
def bin_to_dec_loop(x):
    n = len(x)
    decimal_number = 0
    for i in x:
        decimal_number += (2 ** (n - 1)) * int(i)
        n = n - 1
    return decimal_number

x = str(input("Enter a binary number: "))
print("Decimal (using loop):", bin_to_dec_loop(x))