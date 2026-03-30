import sys
input = sys.stdin.readline

#5, 6, 7, 1, 2, 5, 4

n = int(input())
ls=list(map(int,input().split()))
lis=[ls[0]]

for i in range(1,n):
  k = ls[i]
  if(k > lis[-1]):
    lis.append(k)
  else:
    left = 0
    right = len(lis) - 1
    while left <= right:
      mid = (left + right) // 2
      if lis[mid] < k:
        left = mid + 1
      else:
        right = mid - 1
    lis[left] = k
print(len(lis))