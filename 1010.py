def fac(n):
  k=1
  for i in range(1,n+1):
    k*=i
  return k
for _ in range(int(input())):
  b,a=map(int,input().split())
  print(fac(a)//(fac(b)*fac(a-b)))