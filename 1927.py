import sys
import heapq
input = sys.stdin.readline

hq = []

for _ in range(int(input())):
    a = int(input())

    if a == 0:
        if not hq:
            print(0)
        else:
            print(heapq.heappop(hq))
    else:
        heapq.heappush(hq, a)