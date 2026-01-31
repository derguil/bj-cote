b,a=map(int,input().split())
c=[]
d=[]
for i in range(b):
  c.append(list(map(int,input().split())))
for i in range(b):
  d.append(list(map(int,input().split())))
for i in range(b):
  for j in range(a):
    c[i][j]+=d[i][j]
for i in range(b):
  print(*c[i])