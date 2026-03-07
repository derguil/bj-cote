import sys
input = sys.stdin.readline

n = int(input())
ls=list(map(int,input().split()))

dp = [1]*n

for i in range(1,n):
  prevmaxdp=0
  for j in range(i):
    if(ls[j]<ls[i]):
      prevmaxdp=max(prevmaxdp,dp[j])

  dp[i]=prevmaxdp+1
  
print(max(dp))