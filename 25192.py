c=set()
res=0
for _ in range(int(input())):
  i=input()
  if(i == "ENTER"):
    res+=len(c)
    c.clear()
  else:
    c.add(i)
res+=len(c)
print(res)