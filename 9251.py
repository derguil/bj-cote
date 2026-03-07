import sys
input = sys.stdin.readline

a=list(input().rstrip())
b=list(input().rstrip())
la=len(a)
lb=len(b)

dp = [[0]*(lb+1) for _ in range(la+1)]

for i in range(1,la+1):
  for j in range(1,lb+1):
    if(a[i-1]==b[j-1]):
      dp[i][j]=dp[i-1][j-1]+1
    elif(a[i-1]!=b[j-1]):
      dp[i][j]=max(dp[i][j-1],dp[i-1][j])

print(max(max(row) for row in dp))
