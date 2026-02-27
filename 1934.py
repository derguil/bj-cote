for _ in range(int(input())):
  a,b=map(int, input().split())
  c=a*b
  while b:
    a,b=b,a%b
  print(c//a)





