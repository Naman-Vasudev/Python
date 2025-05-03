string="My name is naman"

reversed_string=""
for i in range(len(string)-1,-1,-1):
    reversed_string=reversed_string+string[i]

print(reversed_string)
string = "My name is naman"
reversed_string = ''.join(reversed(string))  # Join the reversed characters
print(reversed_string)