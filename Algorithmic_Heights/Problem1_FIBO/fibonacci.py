def fib(n):
    if n == 0:
        return 0
    elif n < 3:
        return 1
    else:
        return fib(n-1)+fib(n-2)

def fibIterative(n):
    fib = [0,1,1]
    if n < 3:
        return fib[n]
    else:
        for i in range(3,n+1):
            fib.append(fib[i-1] + fib[i-2])
        return fib[n]
print(fib(24))
print(fibIterative(24))
