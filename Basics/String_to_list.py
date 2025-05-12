# ================================================================
# String to List Conversion Methods in Python
# ================================================================

# Sample string
s = "bbfdvbldfldff"

# ----------------------------------------------------------------
# 1. Convert string to list of characters using list()
# ----------------------------------------------------------------
char_list = list(s)
print("1. list() method:", char_list)
# Output: ['b', 'b', 'f', 'd', 'v', 'b', 'l', 'd', 'f', 'l', 'd', 'f', 'f']


# ----------------------------------------------------------------
# 2. Using List Comprehension to convert string to list of chars
# ----------------------------------------------------------------
char_list_comp = [char for char in s]
print("2. List comprehension method:", char_list_comp)


# ----------------------------------------------------------------
# 3. Split a string using a delimiter (split())
# ----------------------------------------------------------------
csv_string = "apple,banana,grape"
split_list = csv_string.split(",")
print("3. Split by comma:", split_list)
# Output: ['apple', 'banana', 'grape']

space_string = "hello world from python"
split_space = space_string.split()  # Default split by space
print("   Split by space:", split_space)


# ----------------------------------------------------------------
# 4. Split into fixed-size chunks using slicing
# ----------------------------------------------------------------
chunk_size = 2
chunks = [s[i:i+chunk_size] for i in range(0, len(s), chunk_size)]
print("4. Chunks of size 2:", chunks)
# Output: ['bb', 'fd', 'vb', 'ld', 'fl', 'df', 'f']


# ----------------------------------------------------------------
# 5. Split into fixed-size chunks with padding on the last chunk
# ----------------------------------------------------------------
chunk_size = 3
padded_chunks = [s[i:i+chunk_size].ljust(chunk_size, '_') for i in range(0, len(s), chunk_size)]
print("5. Chunks of size 3 with padding:", padded_chunks)
# Output: ['bbf', 'dvb', 'ldf', 'ldf', 'f__']


# ----------------------------------------------------------------
# 6. Using re.findall() for regex-based chunking
# ----------------------------------------------------------------
import re
regex_chunks = re.findall('.{1,3}', s)
print("6. Regex chunks (size ≤ 3):", regex_chunks)
# Output: ['bbf', 'dvb', 'ldf', 'ldf', 'f']


# ----------------------------------------------------------------
# BONUS: Custom function to split a string into chunks
# ----------------------------------------------------------------
def split_fixed_chunks(string, size, pad=False, pad_char='_'):
    """
    Split string into chunks of given size.
    Args:
        string (str): input string
        size (int): chunk size
        pad (bool): whether to pad last chunk
        pad_char (str): character to pad with
    Returns:
        list: list of string chunks
    """
    if pad:
        return [string[i:i+size].ljust(size, pad_char) for i in range(0, len(string), size)]
    else:
        return [string[i:i+size] for i in range(0, len(string), size)]

print("7. Custom function (no padding):", split_fixed_chunks(s, 4))
print("   Custom function (with padding):", split_fixed_chunks(s, 4, pad=True))
