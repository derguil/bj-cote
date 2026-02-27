from collections import deque

n, k = map(int, input().split())
q = deque(range(1, n+1))
b = []

while q:
    q.rotate(-(k-1))
    b.append(q.popleft())

print("<" + ", ".join(map(str, b)) + ">")