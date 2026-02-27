a,b=map(int,input().split())
c, d = set(), set()

for _ in range(a):
  c.add(input())

for _ in range(b):
  d.add(input())

e=list(c&d)
e.sort()
print(len(e))
for i in e:
  print(i)