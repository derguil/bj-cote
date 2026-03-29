from collections import defaultdict

n=int(input())
k=int(input())

ls = defaultdict(list)

for i in range(1,n+1):
  for j in range(1,n+1):
    ls[i*j].append((i-1)*n + j)
print(ls)
for key, values in ls.items():
  if k in values:
    print(key)
    break

