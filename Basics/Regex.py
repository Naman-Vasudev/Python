'''
Regular Expression (Regex)
• Regular expressions are the sequence of patterns that are used to extract patterns in data.
• You can also use this for matching and searching patterns. Awesome right!
• Let's see Regex in action

'''

#import regex module
import re
#input data
demo ="jhk1pi2yt3wx4x5iss6's7unaj8;ss9jshosjsss,susiw.su"
'''Use the regex to extarct numbers out
Input data.
To extract the numbers you can use [0-9] pattern'''

r = re.findall("[0-9]", demo)
print(type(r)) #LIST
#print the output 
print(''.join(r))
