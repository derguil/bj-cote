import sys
input=sys.stdin.readline

abcls=[[[-1 for _ in range(51)] for _ in range(51)] for _ in range(51)]

def w(a,b,c):
  if(a<=0 or b<=0 or c<=0):
    return 1
  elif(a > 20 or b > 20 or c > 20):
    abcls[a][b][c]=w(20,20,20)
  elif abcls[a][b][c] != -1:
    return abcls[a][b][c]
  elif(a < b and b < c):
    abcls[a][b][c]=w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
  else:
    abcls[a][b][c]=w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
  return abcls[a][b][c]

while True:
  a,b,c=map(int,input().split())
  if(a==b==c==-1):
    break
  print(f"w({a}, {b}, {c}) = " + str(w(a,b,c)))