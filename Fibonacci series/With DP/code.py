import sys

def fibonacci(n):
    if n== 0  or n == 1:
        return n
    else:
        if(table[n-2]==n):
            table[n-2]= fibonacci(n-2)
            if table[n-1]== None:
                table[n]=table[n-1]+table[n-2]
                return table[n]
        table[n]=table[n-1]+table[n-2]
        return table[n]


n = int(input().strip())
print(fibonacci(n))
table =[]