sample_list = [1, "apple", 2, "banana", "apple", 1, 2, 3]
sum=0
product=1
for element in sample_list:
    if type(element)==int:
        sum=sum+element
        product=product*element

print("Sum is ",sum)
print("Product is ",product)



import numpy as np
int_list = [x for x in sample_list if type(x) == int]
sum_of_list=np.sum(int_list)
product_of_list=np.prod(int_list)
print("Sum is ",sum_of_list)
print("Product is ",product_of_list)

while(1>0):
    print("naman")