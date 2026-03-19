while True:
  n, *ls = list(map(int,input().split()))
  if(n == 0):
    break

  res = ls[0]
  stack = [ls[0]]
  for i in range(1,n):
    if(stack[-1] >= ls[i]):
      width = 1
      height = stack[-1]
      for j in stack[::-1]:
        if(height > j):
          height = j
        res = max(res, width*height)
        width += 1
    stack.append(ls[i])
  width = 1
  height = stack[-1]
  for j in stack[::-1]:
    if(height > j):
      height = j
    res = max(res, width*height)
    width += 1

  print(res)