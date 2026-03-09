import sys
input=sys.stdin.readline

s=input().strip()
q=int(input())
sumls=[[0] for _ in range(ord('a'), ord('z')+1)]
for sumlsnodeidx in range(ord('z')+1-ord('a')):
  for i in s:
    if(ord(i)==sumlsnodeidx+ord('a')):
      sumls[sumlsnodeidx].append(sumls[sumlsnodeidx][-1]+1)
    else:
      sumls[sumlsnodeidx].append(sumls[sumlsnodeidx][-1])

for _ in range(q):
  char,start,end = input().split()
  start=int(start)
  end=int(end)
  
  print(sumls[ord(char)-ord('a')][end+1]-sumls[ord(char)-ord('a')][start])