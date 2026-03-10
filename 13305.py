import sys
input=sys.stdin.readline

n=int(input())
roads=list(map(int,input().split()))
oils=list(map(int,input().split()))

res=0
curroilprice=oils[0]

for i in range(len(oils)-1):
  if(oils[i] < curroilprice):
    curroilprice = oils[i]
  res+=curroilprice*roads[i]

print(res)