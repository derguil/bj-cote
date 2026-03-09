import math
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
ls=list(map(int,input().split()))
sumls=[0]
for i in range(n):
  sumls.append(sumls[-1]+ls[i])
res=[0]*m
for i in sumls:
  for j in range(m):
    if(i%m==j):
      res[j]+=1
f=0
for i in res:
  f+=math.comb(i,2)
print(f)