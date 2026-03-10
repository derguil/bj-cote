import sys
input=sys.stdin.readline

n,k=map(int,input().split())
ls=[int(input()) for _ in range(n)]

res=0
for i in ls[::-1]:
  if(k//i>0):
    res+=k//i
    k%=i
print(res)