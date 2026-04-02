import sys
import heapq
input = sys.stdin.readline

hq = []
hqls=[]

for _ in range(int(input())):
  a = int(input())

  if a == 0:
    if not hq:
      print(0)
    else:
      print(heapq.heappop(hq)[1])

  else:
    heapq.heappush(hq, (abs(a),a))