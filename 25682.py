import sys
input=sys.stdin.readline

n,m,k=map(int,input().split())

ls=[list(input().strip()) for _ in range(n)]
sumWls = [[0]*(m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        x = i - 1
        y = j - 1

        if (x + y) % 2 == 0:
            val = 1 if ls[x][y] != 'W' else 0
        else:
            val = 1 if ls[x][y] != 'B' else 0

        sumWls[i][j] = sumWls[i-1][j] + sumWls[i][j-1] - sumWls[i-1][j-1] + val

mins=k**2

for i in range(1, n-k+2):
    for j in range(1, m-k+2):
        repaintW = sumWls[i+k-1][j+k-1] - sumWls[i-1][j+k-1] - sumWls[i+k-1][j-1] + sumWls[i-1][j-1]
        repaintB = k*k - repaintW

        mins=min(mins,repaintW,repaintB)

print(mins)