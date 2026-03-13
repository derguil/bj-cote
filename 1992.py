n = int(input())
ls = [list(input()) for _ in range(n)]
colorls=[]

def req(x, y, size):
  color = ls[x][y]
  for i in range(x, x + size):
    for j in range(y, y + size):
      if ls[i][j] != color:
        half = size // 2
        colorls.append('(')
        req(x, y, half)
        req(x, y + half, half)
        req(x + half, y, half)
        req(x + half, y + half, half)
        colorls.append(')')
        return

  if color == '0':
    colorls.append('0')
  else:
    colorls.append('1')

req(0, 0, n)
print("".join(colorls))