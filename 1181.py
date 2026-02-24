a=[]
for _ in range(int(input())):
  a.append(input())
a=list(set(a))
a.sort(key=lambda x: (len(x), x))
print(*a, sep="\n")