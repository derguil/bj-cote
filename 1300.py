from collections import defaultdict

n=int(input())
k=int(input())

start = 1
end = n**2

res = 0

while start <= end:
  mid = (start + end)//2

  count = 0
  for i in range(1,n+1):
    count += min(mid // i, n)
  # print(count)

  if(count >= k):
    res = mid
    end = mid-1
  else:
    start = mid+1

print(res)
