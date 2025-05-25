def is_prime(x):
    if x<=1:
        return False
    for i in range(2,(x//2)+1):
        if x%i==0:
            return False
    else:
        return True
x=int(input("Enter a number please: "))
if is_prime(x)==False:
    print("Not Prime")
else:
    print("Prime")

#Printing first n prime numbers
n=int(input("Enter n: "))
count=0
prime=2
while count<n:
    if is_prime(prime)==True:
        print(prime)
        count+=1
    prime+=1