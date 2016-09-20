# Uses python2
import sys

def get_fibonacci_last_digit(n):
    a = []
    #print (n)
    if(n <= 1):
        a.append(n)
        return (a[n]%10)
    else:
        a.append(0)
        a.append(1)
        #print (a)
        for i in range(2,n+1):
           a.append((a[i-1] +a[i-2])%10)
           #print (i)
        return (a[n])
    

if __name__ == '__main__':
    #input = sys.stdin.read()
    #print (input)
    n = int(raw_input())
    print(get_fibonacci_last_digit(n))
