def countBitsFlip(a, b):
    a_xor_b=bin(a^b)[2:]
    count=0
    for i in a_xor_b:
        if i=='1':
            count+=1
    return count    
a=int(input("enter a: "))
b=int(input("enter b: "))
print(countBitsFlip(a,b))