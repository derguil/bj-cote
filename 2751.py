a=[]
for _ in range(int(input())):
  a.append(int(input()))
a.sort()
print(*a, sep='\n')