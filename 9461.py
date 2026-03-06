import sys
input=sys.stdin.readline

for _ in range(int(input())):
  n=int(input())
  ls=[1,1,1,2,2]
  for i in range(5,n):
    ls.append(ls[i-1]+ls[i-5])
  print(ls[n-1])