import sys
input=sys.stdin.readline

def can(n,start,term,end):
  if(n==1):
    print(start,end)
    return
  can(n-1,start,end,term)
  print(start,end)
  can(n-1,term,start,end)

n=int(input())
print(2**n-1)
can(n,1,2,3)