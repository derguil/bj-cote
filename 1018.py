n,m=list(map(int,input().split()))
a=[[] for _ in range(n)]
for i in range(n):
  a[i] = list(input())

board = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]

c=n*m
for i in range(n-7):
  for j in range(m-7):
    dif=0
    for k in range(8):
      for l in range(8):
        if(a[i+k][j+l] != board[k][l]):
          dif+=1
    if(min(dif,64-dif) < c):
      c=min(dif,64-dif)

print(c)