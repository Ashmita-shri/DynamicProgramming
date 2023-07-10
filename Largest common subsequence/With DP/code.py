import sys

def longest_common_subsequence(m,n):
    for i in range(m+1):
        for j in range(n+1):
            if str1[m] == str2[n]:
                t[i][j]=1+t[i-1][j-1]
            else:
                a=t[i-1][j]
                b=t[i][j-1]
                t[i][j]=max(a,b)
    return t





print('Enter first string')
str1=input()
print('Enter second string')
str2=input()
t=[]
# For writting longest common subsequence problem , we save the value in table using  row major o column major order on writting non recursive program
answer=longest_common_subsequence((len(str1)-1),(len(str2)-1))
print(answer)
