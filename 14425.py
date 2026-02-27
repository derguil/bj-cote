a,b=map(int,input().split())
c, d = [], []
e=0

for _ in range(a):
  c.append(input())

for _ in range(b):
  d.append(input())


for i in c:
  if i in d:
    e += 1

print(e)