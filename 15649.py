import sys
input=sys.stdin.readline

n,m=map(int,input().split())
ls=[]

def addls(depth):
  if(depth==m):
    print(*ls)
    return
  for i in range(1,n+1):
    if(i in ls):
      continue
    ls.append(i)
    addls(depth+1)
    ls.pop()

addls(0)