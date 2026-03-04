import sys
input=sys.stdin.readline

n = int(input())
pwr=[[0]*n for _ in range(n)]
for i in range(n):
  pwr[i]=list(map(int,input().split()))

team=[]
teams=[]

def dfs(start, depth):
  if depth == n//2:
    teams.append(team[:])
    return
  for i in range(start, n+1):
    team.append(i)
    dfs(i+1, depth+1)
    team.pop()

dfs(1, 0)

all_set = set(range(1, n+1))
pointdifmin = 1000

def score(t):
  s = 0
  for i in range(len(t)):
    for j in range(i+1, len(t)):
      a, b = t[i]-1, t[j]-1
      s += pwr[a][b] + pwr[b][a]
  return s

for t in teams:
  link = list(all_set - set(t))
  sp = score(t)
  lp = score(link)
  pointdifmin = min(pointdifmin, abs(sp - lp))

print(pointdifmin)