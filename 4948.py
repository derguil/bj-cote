while True:
  c=int(input())
  if(c==0):
    break
  k=0
  for a in range(c+1,2*c+1):
    isS=True
    if(a==1):
      isS=False
    for i in range(2, int(a**0.5) + 1):
      if(a%i==0):
        isS=False
        break
    if(isS==True):
      k+=1
  print(k)