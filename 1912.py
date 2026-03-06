import sys
input=sys.stdin.readline

n=int(input())
ls=list(map(int,input().split()))

globalv=localv=ls[0]
for i in range(1,n):
  localv=max(ls[i],localv+ls[i])
  globalv=max(localv,globalv)

print(globalv)