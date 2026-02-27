b=[]
for _ in range(int(input())):
  a=int(input())
  if(a==0):
    b.pop()
  else:
    b.append(a)
print(sum(b))