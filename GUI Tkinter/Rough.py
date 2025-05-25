import math
def is_prime(x):
    if x==0 or x==1:
        return False
    for i in range(2,int(math.sqrt(x))+1):
            if x%i==0:
                 return False
            else:
                 return True
    

n=int(input("Enter n for how many first n primes you wanna know: "))
count=0
prime=2
while count!=n:
     if is_prime(prime)==True:
          print(prime)
          prime+=1
          count+=1

     
