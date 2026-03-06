import sys
input=sys.stdin.readline

n=int(input())
ls=1
ls22=2
for i in range(2,n):
  ls,ls22 = ls22,(ls+ls22)%15746

if(n==1):
  print(1)
elif(n==2):
  print(2)
else:
  print(ls22)