import sys

def longest_common_subsequence(m,n):
    if m==0 or n==0:
        return 0
    else:
        if str1[m]== str2[n]:
            return 1+longest_common_subsequence(m-1,n-1)
        else:
            a=longest_common_subsequence(m-1,n)
            b=longest_common_subsequence(m,n-1)
            c=max(a,b)
            return c


print('Enter first string')
str1=input()
print('Enter second string')
str2=input()
answer=longest_common_subsequence((len(str1)-1),(len(str2)-1))
print(answer)
