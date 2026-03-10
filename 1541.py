import sys
input=sys.stdin.readline

s = input().split('-')
ans = sum(map(int, s[0].split('+')))
for part in s[1:]:
  ans -= sum(map(int, part.split('+')))

print(ans)