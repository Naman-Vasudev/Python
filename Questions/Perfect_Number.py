def is_perfect(x):
    sum=0
    for i in range(1,x//2+1):
        if x%i==0:
            sum+=i
            if sum>x:
                return False
            
    
    if sum==x:
        return True

x=int(input("Enter a number: "))

if is_perfect(x)==True:
    print("The number is perfect")
else:
    print("Not perfect")


# num=2
# while 1<2 and num%2==0 and num<10000000000000000000000000000000000:
#     num+=2
#     if is_perfect(num)==True:
#         print(num)
