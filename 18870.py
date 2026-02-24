n = int(input())
b = list(map(int, input().split()))
c = sorted(set(b))
d = {c[i]: i for i in range(len(c))}
e = []
for x in b:
  e.append(d[x])

print(*e)