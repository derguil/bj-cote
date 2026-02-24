a=[]
for _ in range(int(input())):
  b,c = input().split()
  a.append([int(b),c])
a.sort(key=lambda x: (x[0]))
for b,c in a:
  print(b,c)