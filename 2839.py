n=int(input())
c = 0
iss = False
for i in range(n//5, -1, -1):
  if((n - 5*i) % 3 == 0):
    c = i + (n - 5*i)//3
    iss=True
    break

if(iss):
  print(c)
else:
  print(-1)