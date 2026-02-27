for _ in range(int(input())):
  a=int(input())
  while True:
    isS=False
    for i in range(2, int(a**0.5) + 1):
      if(a%i==0):
        isS=True
        break
    if(isS==False):
      break
    a+=1
  print(a)