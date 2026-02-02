a,b=input().split()
b=int(b)
c=[]
d=0
e=list(map(str, [0,1,2,3,4,5,6,7,8,9]))
for i in a:
  if(i in e):
    c.append(int(i))
  else:
    c.append(ord(i)-55)
c.reverse()
for i in range(len(c)):
  d+=c[i]*(b**i)



print(d)