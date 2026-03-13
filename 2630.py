n = int(input())
ls = [list(map(int, input().split())) for _ in range(n)]

white = 0
black = 0

def req(x, y, size):
  global white, black

  color = ls[x][y]
  for i in range(x, x + size):
    for j in range(y, y + size):
      if ls[i][j] != color:
        half = size // 2
        req(x, y, half)
        req(x, y + half, half)
        req(x + half, y, half)
        req(x + half, y + half, half)
        return

  if color == 0:
    white += 1
  else:
    black += 1

req(0, 0, n)
print(white)
print(black)