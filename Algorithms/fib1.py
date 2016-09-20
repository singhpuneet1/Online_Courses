# Uses python3
import datetime
def calc_fib(n):
    a = []
    if(n <= 1):
        a.append(n)
        return a(len(a))
    else:
        a.append(0)
        a.append(1)
        for i in range(2,n+1):
           a.append(a[i-1] +a[i-2])
        return a[n]

a = datetime.datetime.now()
n = int(input())
print(calc_fib(n))
b = datetime.datetime.now()
c= b-a
print (c.seconds)
