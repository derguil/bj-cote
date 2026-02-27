c=set()
for _ in range(int(input())):
  a,b=input().split()
  if(b=="enter"):
    c.add(a)
  else:
    c.remove(a)
c=sorted(list(c))[::-1]
# print(c)
for i in c:
  print(i)
