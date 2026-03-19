n = int(input())
ls = [list(map(int, input().split())) for _ in range(n)]

m1 = 0
yn = 0
p1 = 0

def req(x, y, size):
  global m1,yn,p1

  color = ls[x][y]
  for i in range(x, x + size):
    for j in range(y, y + size):
      if ls[i][j] != color:
        s = size//3
        for p in range(3):
          for q in range(3):
            req(x+s*p,y+s*q,s)
        return

  if color == -1:
    m1+=1
  elif color == 0:
    yn+=1
  else:
    p1+=1

req(0, 0, n)
print(m1)
print(yn)
print(p1)