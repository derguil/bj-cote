q,w=map(int, input().split())
e,r=map(int, input().split())

a=c=q*r+e*w
b=d=w*r

while b:
  a,b=b,a%b

print(c//a, d//a)