import sys
input = sys.stdin.readline

n = int(input())
ls=[]
for _ in range(n):
  ls.append(int(input()))

if n == 1:
  print(ls[0])
elif n == 2:
  print(ls[0] + ls[1])
else:
  dp = [0] * n
  dp[0] = ls[0]
  dp[1] = ls[0] + ls[1]
  dp[2] = max(ls[0] + ls[1], ls[0] + ls[2], ls[1] + ls[2])

  for i in range(3, n):
    dp[i] = max(dp[i-1], dp[i-2] + ls[i], dp[i-3] + ls[i-1] + ls[i])

  print(dp[n-1])
  