# --------------------------------------------------
# String Methods in Python - With Examples & Output
# --------------------------------------------------

# Sample text for basic demonstrations
text = "I am a coder."

# 1. endswith()
# Checks if the string ends with the given substring
print(text.endswith("er."))  # Output: True

# 2. capitalize()
# Capitalizes the first character of the string
print(text.capitalize())  # Output: I am a coder.

# 3. replace()
# Replaces all occurrences of a substring with another
print(text.replace("coder", "developer"))  # Output: I am a developer.

# 4. find()
# Returns the index of the first occurrence of the substring
print(text.find("am"))  # Output: 2

# 5. count()
# Returns the number of times a substring appears in the string
print(text.count("am"))  # Output: 1


# ----------------------------------------
# Case Conversion and Case Checks
# ----------------------------------------

string = "He's name is Naman. Naman is an honest man."

# 6. upper()
# Converts all characters to uppercase
print(string.upper())  # Output: HE'S NAME IS NAMAN. NAMAN IS AN HONEST MAN.

# 7. lower()
# Converts all characters to lowercase
print(string.lower())  # Output: he's name is naman. naman is an honest man.

# 8. title()
# Capitalizes the first letter of each word
print(string.title())  
# Output: He'S Name Is Naman. Naman Is An Honest Man.

# 9. swapcase()
# Swaps the case: upper -> lower and lower -> upper
str1 = "Python is a Interpreted Language" 
print(str1.swapcase())  
# Output: pYTHON IS A iNTERPRETED lANGUAGE

# 10. isupper()
# Returns True if all characters are uppercase
str2 = "WORLD HEALTH ORGANIZATION"
print(str2.isupper())  # Output: True

# 11. islower()
# Returns True if all characters are lowercase
str3 = "hello world"
print(str3.islower())  # Output: True

# 12. istitle()
# Returns True if the first letter of each word is capitalized
str4 = "World Health Organization"
print(str4.istitle())  # Output: True

str5 = "To kill a Mocking bird"
print(str5.istitle())  # Output: False


# ----------------------------------------
# Whitespace and Formatting Methods
# ----------------------------------------

# 13. strip()
# Removes leading and trailing whitespaces
str6 = "  Silver Spoon  "
print(str6.strip())  # Output: Silver Spoon

# 14. rstrip()
# Removes trailing characters (default is whitespace or user-defined)
str7 = "Hello !!!"
print(str7.rstrip("!"))  # Output: Hello

# 15. center(width, fillchar)
# Centers the string in a field of given width, padded with optional fillchar
str8 = "Welcome to the Console!!!"
print(str8.center(50))  
# Output:             Welcome to the Console!!!

print(str8.center(50, "*"))  
# Output: ************Welcome to the Console!!!************

# Parameter explanation:
# .center(width, fillchar) -> 'width' is total length; 'fillchar' fills extra space


# ----------------------------------------
# String Type Check Methods
# ----------------------------------------

# 16. isalnum()
# Returns True if all characters are alphanumeric (A-Z, a-z, 0-9), no symbols
str9 = "WelcomeToTheConsole"
print(str9.isalnum())  # Output: True

# 17. isalpha()
# Returns True if all characters are alphabetic (A-Z, a-z)
str10 = "Welcome"
print(str10.isalpha())  # Output: True

# 18. isprintable()
# Returns True if all characters in string are printable
str11 = "We wish you a Merry Christmas"
print(str11.isprintable())  # Output: True

# 19. isspace()
# Returns True if string contains only whitespace (space, tab, etc.)
str12 = "        "  # Using Spacebar
print(str12.isspace())  # Output: True

str13 = "\t\t"  # Using Tabs
print(str13.isspace())  # Output: True


# ----------------------------------------
# Start Check
# ----------------------------------------

# 20. startswith()
# Checks if the string starts with the specified value
str14 = "Python is a Interpreted Language"
print(str14.startswith("Python"))  # Output: True


# ----------------------------------------
# Extra Examples Using 'count' and 'find'
# ----------------------------------------

sample = "He's name is Naman. Naman is an honest man."

# 21. count(substring)
print(sample.count("name"))  # Output: 2
print(sample.count("n"))     # Output: 4

# 22. find(substring)
print(sample.find("Naman"))  # Output: 13
print(sample.find("Unknown"))  # Output: -1 (not found)
