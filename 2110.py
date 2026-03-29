import sys
input=sys.stdin.readline

n,c=map(int, input().split())
ls=list(int(input()) for _ in range(n))
ls.sort()

start = 1
end = ls[-1]

res=0

while start <= end:
  # print(start,end)
  midc = (start+end)//2 #거리

  count = 1
  last = ls[0]

  for i in range(1, n):
    if ls[i] - last >= midc:
      count += 1
      last = ls[i]

  if(count < c):
    end = midc-1
  else:
    res = midc
    start = midc+1
  
print(res)