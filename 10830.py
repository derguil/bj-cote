import sys
input = sys.stdin.readline

n, b = map(int, input().split())
ls = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
  for j in range(n):
    ls[i][j] %= 1000

def mul(a, b):
    res = [[0] * n for _ in range(n)]
    for i in range(n):
      for k in range(n):
        for j in range(n):
          res[i][k] += a[i][j] * b[j][k]
        res[i][k] %= 1000
    return res

def req(mat, power):
    if power == 1:
      return mat

    half = req(mat, power // 2)
    
    if power % 2 == 0:
      return mul(half, half)
    else:
      return mul(mul(half, half), mat)

answer = req(ls, b)

for row in answer:
    print(*row)