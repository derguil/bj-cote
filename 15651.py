import sys
input=sys.stdin.readline

n,m=map(int,input().split())
ls=[]

def addls(depth):
  if(depth==m):
    print(*ls)
    return
  for i in range(1,n+1):
    # if(ls):
    #   if(i <= ls[-1]):
    #     continue
    ls.append(i)
    addls(depth+1)
    ls.pop()

addls(0)