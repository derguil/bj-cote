n=int(input())
isS=False

for i in range(n):
  a = sum(map(int, list(str(i))))
  if(i + a == n):
    print(i)
    isS = True
    break

if(isS==False):
  print(0)

