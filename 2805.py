import sys
input=sys.stdin.readline

n, m = map(int,input().split())
ls = list(map(int,input().split()))

start = 1
end = max(ls)
res = 0

while start <= end:
  mid = (start+end)//2
  resn = 0
  for i in ls:
    ff = i - mid
    if(ff > 0):
      resn += ff

  if(resn >= m):
    res = mid
    start = mid + 1
  else:
    end = mid - 1

print(res)