n=int(input())
ls=[b for a,b in sorted([list(map(int,input().split())) for _ in range(n)],key=lambda x: (x[0]))]

dp = [1]*n
for i in range(1,n):
  for j in range(i):
    if(ls[j]<ls[i]):
      dp[i]=max(dp[i],dp[j]+1)

print(n-max(dp))