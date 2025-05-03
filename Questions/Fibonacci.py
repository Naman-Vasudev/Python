def nth_term_fibonacci(x):
    if x==1:
        return 0
    if x==2:
        return 1
    else:
        return nth_term_fibonacci(x-2)+nth_term_fibonacci(x-1)

x=int(input("Enter n upto which you want series: "))

fibonnaci_series=[]
for i in range(1,x+1):
    fibonnaci_series.append(nth_term_fibonacci(i))

print(fibonnaci_series)

def fibonacci_series(x):
    series = []
    a, b = 0, 1
    for i in range(x):
        series.append(a)
        a, b = b, a + b
    return series

x = int(input("Enter n up to which you want series: "))
print(fibonacci_series(x))

