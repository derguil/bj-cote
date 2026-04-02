import sys
import heapq
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  M = int(input())
  ls = []
  while len(ls) < M:
    ls.extend(map(int, input().split()))

  minhq=[ls[0]]             
  maxhq=[]
  res=[ls[0]]

  for i in range(1,M):
    if(ls[i] > minhq[0]):
      heapq.heappush(minhq,ls[i])
    else:
      heapq.heappush(maxhq,-ls[i])

    if(len(minhq) > len(maxhq)+1):
      heapq.heappush(maxhq, -heapq.heappop(minhq))
    elif(len(minhq) < len(maxhq)):
      heapq.heappush(minhq, -heapq.heappop(maxhq))

    if(i%2==0):
      a=minhq[0]
      res.append(a)

  print(len(res))
  for i in range(len(res)//10+1):
    print(*res[i*10:(i+1)*10])
      