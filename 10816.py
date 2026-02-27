int(input())
a=list(map(int,input().split()))
int(input())
b=list(map(int,input().split()))
c={}

for i in a:
  if i in c:
    c[i]+=1
  else:
    c[i]=1



for i in b:
  if i in c:
    print(c[i], end=" ")
  else:
    print(0, end=" ")