import sys
input=sys.stdin.readline

k,n=map(int, input().split())
ls=sorted(list(int(input()) for _ in range(k)))

df=sum(ls)//n

for i in range(df,0,-1):
  resn=0
  for node in ls:
    resn+=node//i
  if(resn >= n):
    print(i)
    break
    