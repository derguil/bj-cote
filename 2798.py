a,sum=map(int,input().split())
b=list(map(int,input().split()))
c=0

for i in range(a):
  for j in range(i+1, a):
    for k in range(j+1, a):
      if sum >= b[i]+b[j]+b[k] > c:
        c = b[i]+b[j]+b[k]

print(c)