for _ in range(int(input())):
  b=[]
  isS=True
  a=list(input())
  for i in a:
    if(i=="("):
      b.append(1)
    else:
      if b:
        b.pop()
      else:
        isS=False
        break
  if(len(b)!=0):
    isS=False

  if(isS==True):
    print("YES")
  else:
    print("NO")