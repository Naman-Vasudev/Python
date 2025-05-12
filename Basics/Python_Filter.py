'''
Python Filter
The filter function is a python's built-in function that you can use to iterate over the elements. It will return the items as per the defined condition.
'''
list_1=[1,2,3,4,5,6,7,8,9,10,11]

def even(number):
    return number%2==0
output=filter(even,list_1)

print(type(output))
print(list(output))