from collections import deque

n = int(input())
moves = list(map(int, input().split()))

ballons = deque((i+1, moves[i]) for i in range(n))
result = []

while ballons:
  idx, move = ballons.popleft()
  result.append(idx)

  if not ballons:
    break
  
  if move > 0:
    ballons.rotate(-(move-1))
  else:
    ballons.rotate(-move)

print(*result)