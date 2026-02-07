a=int(input())
c=[]
for j in range(2,a+1):
  while(a%j==0):
    c.append(j)
    a/=j

for i in c:
  print(i)
  


