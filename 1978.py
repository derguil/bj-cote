c=0
d=list(map(int,input().split()))
for a in d:
  b=0
  for i in range(1,a+1):
    if(a%i==0):
      b+=1
  if(b==2):
    c+=1

print(c)