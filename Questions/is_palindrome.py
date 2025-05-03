input_str = input("Enter a string: ")

if input_str == input_str[::-1]:
    print("It is a palindrome")
else:
    print("It is not a palindrome")

input_str = input("Enter a string: ")

is_palindrome = True

for i in range(len(input_str) // 2):
    if input_str[i] != input_str[-(i + 1)]:
        is_palindrome = False
        break

if is_palindrome:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
