def sum_of_digits(x):
    total=0
    x=abs(x)
    while x!=0:
        
        ld=x%10
        x=x//10
        total=total+ld
    return total

number=int(input("Enter a number: "))
print("The sum of digits is ",sum_of_digits(number))


def sum_of_digits_recursion(x):
    x = abs(x)

    if x == 0:
        return 0
    else:
        return (x % 10) + sum_of_digits_recursion(x//10)


number = int(input("Enter a number: "))
print("The sum of digits is", sum_of_digits_recursion(number))