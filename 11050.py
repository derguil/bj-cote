n,k=map(int,input().split())

def fac(n):
  k=1
  for i in range(1,n+1):
    k*=i
  return k

print(fac(n)//(fac(k)*fac(n-k)))