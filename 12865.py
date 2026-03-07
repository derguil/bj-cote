n,k=map(int,input().split())
ls=[]
for _ in range(n):
  ls.append(list(map(int,input().split())))

dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(1,n+1):
  weight, value = ls[i - 1]
  for j in range(1,k+1):
    if weight <= j:
      dp[i][j] = max(value + dp[i - 1][j - weight], dp[i - 1][j])
    else:
      dp[i][j] = dp[i - 1][j]

print(dp[i][j])