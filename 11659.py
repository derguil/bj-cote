import sys
input=sys.stdin.readline

n,m=map(int,input().split())
ls=list(map(int,input().split()))
sumls=[0]
for i in range(n):
  sumls.append(sumls[-1]+ls[i])
for _ in range(m):
  a,b=map(int,input().split())
  print(sumls[b]-sumls[a-1])