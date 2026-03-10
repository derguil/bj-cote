import sys
input=sys.stdin.readline

n=int(input())
ls=sorted(list(map(int,input().split())))
res=0
for i in range(1,n+1):
  res+=ls[i-1]*(n+1-i)

print(res)