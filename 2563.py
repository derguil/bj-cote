c=[[0]*100 for _ in range(100)]

for _ in range(int(input())):
  a,b=map(int,input().split())
  for i in range(10):
    for j in range(10):
      c[a+i][b+j] = 1

d=0

for i in range(100):
    for j in range(100):
        if c[i][j]==1:
            d+=1

print(d)
