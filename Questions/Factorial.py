def recursive_fact(x):

    if x==0 or x==1:
        return 1
    fact=x*recursive_fact(x-1)
    return fact

def factorial(x):
    fact = 1  # Start with 1, not x
    for i in range(2, x + 1):  # Loop from 2 to x (inclusive)
        fact *= i
    return fact

x=int(input("Enter a number: "))
print(recursive_fact(x))
print(factorial(x))

