s=[]
for _ in range(int(input())):
  a=list(map(int, input().split()))
  match a[0]:
    case 1:
      s.append(a[1])
    case 2:
      if(len(s)==0):
        print(-1)
      else:
        print(s[-1])
        s.pop()
    case 3:
      print(len(s))
    case 4:
      print(1 if len(s)==0 else 0)
    case 5:
      print(-1 if len(s)==0 else s[-1])