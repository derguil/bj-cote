import sys
input=sys.stdin.readline

n,k=map(int,input().split())
ls=list(map(int,input().split()))
sumls=[0]
for i in range(n):
  sumls.append(sumls[-1]+ls[i])
max=-100*1000000
for i in range(n-k+1):
  pp=sumls[i+k]-sumls[i]
  if(pp>max):
    max=pp



print(max)