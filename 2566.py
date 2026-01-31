c=[]
a=0
b=0
d=0
for _ in range(9):
  c.append(list(map(int,input().split())))
for i in range(9):
  for j in range(9):
    if(c[i][j]>d):
      d=c[i][j]
      a=i
      b=j
print(d)
print(a+1,b+1)