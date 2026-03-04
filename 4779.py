import sys
input=sys.stdin.readline

def can(n):
  if(n==0):
    return "-"
  return can(n-1)+" "*(3**(n-1))+can(n-1)

for line in sys.stdin:
  print(can(int(line)))