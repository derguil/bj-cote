c,b=map(int,input().split())
for a in range(c,b+1):
  isS=True
  if(a==1):
    isS=False
  for i in range(2, int(a**0.5) + 1):
    if(a%i==0):
      isS=False
      break
  if(isS==True):
    print(a)