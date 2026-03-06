import sys
input=sys.stdin.readline

n=int(input())
ls = [list(map(int, input().split())) for _ in range(n)]

for i in range(1,n):
  ls[i][0]+=ls[i-1][0]
  ls[i][len(ls[i])-1]+=ls[i-1][-1]
  for j in range(1,len(ls[i])-1):
    ls[i][j]+=max(ls[i-1][j-1],ls[i-1][j])
  
print(max(ls[n-1]))