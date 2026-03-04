n = int(input())
l=["ChongChong"]
for _ in range(n):
  a,b = input().split()
  if a in l:
    l.append(b)
  elif b in l:
    l.append(a)
print(len(set(l)))