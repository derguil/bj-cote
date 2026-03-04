import sys
input=sys.stdin.readline

def recursion(s, l, r, b):
    if l >= r: return 1, b
    elif s[l] != s[r]: return 0, b
    else: return recursion(s, l+1, r-1, b+1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1, b)


for _ in range(int(input())):
  a=input().strip()
  b=1
  print(*isPalindrome(a))