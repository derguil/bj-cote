f=int(input())
a=list(map(int, input().split()))
e=1
b=[]

for i in a:
  while b and b[-1]==e:
    b.pop()
    e+=1
  if(i==e):
    e+=1
  else:
    b.append(i)
while b and b[-1]==e:
  b.pop()
  e+=1

if(e==f+1):
  print("Nice")
else:
  print("Sad")