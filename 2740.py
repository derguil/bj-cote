import sys
input=sys.stdin.readline

n,m=map(int,input().split())
ls1=[]
for i in range(n):
  ls1.append(list(map(int,input().split())))

M,N=map(int,input().split())
ls2=[]
for i in range(M):
  ls2.append(list(map(int,input().split())))

res = [[0]*N for _ in range(n)]
for i in range(n):
  for j in range(m):
    for k in range(N):
      res[i][k] += ls1[i][j]*ls2[j][k]

for i in res:
  print(*i)