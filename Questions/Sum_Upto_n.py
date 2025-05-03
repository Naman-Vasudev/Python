def sum_upto_n(n):
    total=n
    if n==0:
        return 0
    else:
        while n!=0:
            n=n-1
            total=total+n
        return total

number=int(input("Enter the number upto which sum is desired : "))
print("The sum of numbers from 1 to",number, " is",sum_upto_n(number))

def sum_upto_n_recursive(n):
    if n==0:
        return 0
    else:
        while n !=0:
            return n + sum_upto_n_recursive(n-1)

          
number=int(input("Enter the number upto which sum is desired : "))
print("The sum of numbers from 1 to",number, " is",sum_upto_n_recursive(number))
