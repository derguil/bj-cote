import sys
input=sys.stdin.readline

l=[1,1]
n=int(input())
dinamic=0
for i in range(2,n):
  l.append(l[i-2]+l[i-1])
  dinamic+=1
print(l[n-1],dinamic)