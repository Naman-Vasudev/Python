"""
Python Number Notation Guide
This file demonstrates the various number notations in Python
"""

# DECIMAL NOTATION (Base 10)
# This is the default notation - just write the number as is
decimal_number = 42
print(f"Decimal: {decimal_number}")  # Output: 42

# BINARY NOTATION (Base 2)
# Prefix: 0b or 0B
binary_number = 0b101010  # 42 in binary
print(f"Binary: {binary_number}")  # Output: 42
# Convert decimal to binary string representation
print(f"42 in binary: {bin(42)}")  # Output: 0b101010

# OCTAL NOTATION (Base 8) 
# Prefix: 0o or 0O
octal_number = 0o52  # 42 in octal
print(f"Octal: {octal_number}")  # Output: 42
# Convert decimal to octal string representation
print(f"42 in octal: {oct(42)}")  # Output: 0o52

# HEXADECIMAL NOTATION (Base 16)
# Prefix: 0x or 0X
# Uses digits 0-9 and letters A-F (case insensitive)
hex_number = 0x2A  # 42 in hexadecimal
print(f"Hexadecimal: {hex_number}")  # Output: 42
# Convert decimal to hexadecimal string representation
print(f"42 in hexadecimal: {hex(42)}")  # Output: 0x2a

# SCIENTIFIC NOTATION
# Used for very large or small numbers
# Format: aEb or aeb means a × 10^b
scientific_notation1 = 1.234e5  # 123400.0
scientific_notation2 = 1.234E-4  # 0.0001234
print(f"Scientific notation examples: {scientific_notation1}, {scientific_notation2}")

# UNDERSCORE SEPARATOR
# Python 3.6+ allows underscores in numeric literals for readability
readable_large_number = 1_000_000  # Same as 1000000
readable_binary = 0b1010_0110_1110  # Grouping binary digits
readable_hex = 0xA2_B4_C6  # Grouping hex digits
print(f"Number with underscores: {readable_large_number}")  # Output: 1000000

# COMPLEX NUMBERS
# Format: real + imaginary j
complex_number = 3 + 4j
print(f"Complex number: {complex_number}")
print(f"Real part: {complex_number.real}, Imaginary part: {complex_number.imag}")

# TYPE CONVERSION FUNCTIONS
# int() - Convert to integer
# float() - Convert to floating point
# complex() - Convert to complex number
string_number = "42"
print(f"String to int: {int(string_number)}")
print(f"String to float: {float(string_number)}")
print(f"Int to complex: {complex(10)}")  # 10+0j

# BASE CONVERSION
# int(string, base) - Convert string in given base to decimal
print(f"Binary '101010' to decimal: {int('101010', 2)}")  # 42
print(f"Octal '52' to decimal: {int('52', 8)}")  # 42
print(f"Hex '2A' to decimal: {int('2A', 16)}")  # 42

# BITWISE OPERATIONS NOTATION
x = 0x0F  # 15 in decimal (00001111 in binary)
y = 0x33  # 51 in decimal (00110011 in binary)

# Bitwise AND: &
print(f"0x0F & 0x33 = {hex(x & y)}")  # 0x3 (00000011)

# Bitwise OR: |
print(f"0x0F | 0x33 = {hex(x | y)}")  # 0x3f (00111111)

# Bitwise XOR: ^
print(f"0x0F ^ 0x33 = {hex(x ^ y)}")  # 0x3c (00111100)

# Bitwise NOT: ~ (inverts all bits)
print(f"~0x0F = {hex(~x)}")  # -16 in decimal, but shown as negative hex

# Left shift: <<
print(f"0x0F << 2 = {hex(x << 2)}")  # 0x3c (60 in decimal)

# Right shift: >>
print(f"0x0F >> 2 = {hex(x >> 2)}")  # 0x3 (3 in decimal)

# FLOATING POINT NOTATION
float_decimal = 3.14159
float_scientific = 314.159e-2  # Same as 3.14159
print(f"Float examples: {float_decimal}, {float_scientific}")

# INFINITY AND NAN
import math
positive_infinity = float('inf')
negative_infinity = float('-inf')
not_a_number = float('nan')
print(f"Special values: {positive_infinity}, {negative_infinity}, {not_a_number}")

# BOOLEAN VALUES
# True evaluates to 1, False evaluates to 0 in numeric contexts
true_value = True
false_value = False
print(f"True + 1 = {true_value + 1}")  # 2
print(f"False * 10 = {false_value * 10}")  # 0

# STRING REPRESENTATIONS
num = 42
print(f"str(): {str(num)}")  # "42" - general string conversion
print(f"repr(): {repr(num)}")  # "42" - representation (often the same for numbers)
print(f"format(): {format(num, 'd')}")  # "42" - decimal format
print(f"format(): {format(num, 'x')}")  # "2a" - lowercase hex format
print(f"format(): {format(num, 'X')}")  # "2A" - uppercase hex format
print(f"format(): {format(num, 'b')}")  # "101010" - binary format
print(f"format(): {format(num, 'o')}")  # "52" - octal format

# PRECISION FORMATTING FOR FLOATS
pi = 3.14159265359
print(f"{pi:.2f}")  # 3.14 - 2 decimal places
print(f"{pi:.8f}")  # 3.14159265 - 8 decimal places

# INTEGER DIVISION AND MODULO
print(f"7 / 2 = {7 / 2}")  # 3.5 (true division, returns float)
print(f"7 // 2 = {7 // 2}")  # 3 (floor division, returns int)
print(f"7 % 2 = {7 % 2}")  # 1 (modulo, remainder of division)

# DIVMOD FUNCTION (returns quotient and remainder as a tuple)
print(f"divmod(7, 2) = {divmod(7, 2)}")  # (3, 1)