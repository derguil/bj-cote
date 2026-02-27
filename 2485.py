a=[]
b=[]
for _ in range(int(input())):
  a.append(int(input()))
a.sort()
for i in range(len(a)-1):
  b.append(a[i+1] - a[i])
r=b[0]
for i in b[1:]:
  while i:
    r,i=i,r%i
e=0
for i in b:
  e+=i//r-1
print(e)