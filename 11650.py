c=[]
for _ in range(int(input())):
  a,b=map(int,input().split())
  c.append([a,b])
c.sort(key=lambda x: (x[1], x[0]))
for a, b in c:
  print(a, b)