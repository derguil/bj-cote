import sys
input=sys.stdin.readline

n=int(input())
ls=[list(map(int,input().split())) for _ in range(n)]
ls=sorted(ls, key=lambda x: (x[1],x[0]), reverse=True)
kails=[[-1,-1]]
for _ in range(n):
  i = ls.pop()
  if(i[0]>=kails[-1][1]):
    kails.append(i)
print(len(kails)-1)