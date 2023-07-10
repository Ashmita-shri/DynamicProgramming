import sys


def fibonacci(n):
    if n== 0  or n == 1:
        return n
    else:
        a=fibonacci(n-1)
        b=fibonacci(n-2)
        c=a+b
        return c
n = int(input().strip())
print(fibonacci(n))
