import sys
import heapq
input = sys.stdin.readline

n = int(input())
hq = []

for _ in range(n):
    for x in map(int, input().split()):
        if len(hq) < n:
            heapq.heappush(hq, x)
        else:
            if x > hq[0]:
                heapq.heappush(hq, x)
                heapq.heappop(hq)

print(hq[0])