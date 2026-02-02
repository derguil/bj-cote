a=int(input())
b=1
idx=1
while True:
  if(a >= b and b+idx > a):
    break
  b+=idx
  idx+=1


if(idx%2==0):
  c= a-b+1
  d= idx+1-c
else:
  d= a-b+1
  c= idx+1-d

print(f"{c}/{d}")