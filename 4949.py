while True:
  a=input()
  if(a=="."):
    break
  a=list(a)
  b=[]
  isS=True
  for i in a:
    if(i=="("):
      b.append(1)
    elif(i==")"):
      if b:
        b.pop()
      else:
        isS=False
        break
  if(len(b)!=0):
    isS=False
  # print(b)
  if(isS==True):
    print("yes")
  else:
    print("no")