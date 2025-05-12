# Commonly, we use loops to iterate over the list and print out the elements in it. But, we will see how we can quickly iterate over multiple lists and print out the elements in them. For example the loop method will be as follows-
list_1=[1,2,3,4,5]
list_2=['A','B','C','D','E']

for i in range (0,len(list_1)):
    print(list_1[i],"-",list_2[i])

# A better and safer method is to use Python’s built-in zip() function, which pairs elements from both lists only up to the length of the shorter one, preventing index errors. Python zip() is another python built-in function that can be used to assign different elements from different iterators. • This function will provide output which includes a tuple.

first=['naman','aman','lionel']
second=['vasudev','vasudev','messi']
output=zip(first,second)
print(output) #ZIP OBJECT
print(list(output))

list_1 = [1, 2, 3, 4, 5]
list_2 = ['A', 'B', 'C', 'D', 'E']

for num, char in zip(list_1, list_2):
    print(num, "-", char)

# If you want to explicitly handle unequal lengths and not just stop at the shorter one, you can use itertools.zip_longest():


from itertools import zip_longest

list_1 = [1, 2, 3]
list_2 = ['A', 'B', 'C', 'D']

for num, char in zip_longest(list_1, list_2, fillvalue='-'):
    print(num, "-", char)