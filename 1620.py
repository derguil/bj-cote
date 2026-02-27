a,b=map(int,input().split())
c=[]
d={}
for i in range(a):
  p=input()
  c.append(p)
  d[p] = i

for _ in range(b):
  i=input()
  try:
    k = int(i)
    print(c[k-1])
  except ValueError:
    print(d[i]+1)