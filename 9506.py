a=0
while True:
  a=int(input())
  if(a==-1):
    break
  b=[]
  for i in range(1,(a//2)+1):
    if(a%i==0):
      b.append(i)
  if(sum(b)==a):
    print(f"{a} = " + " + ".join(map(str, b)))
  else:
    print(f"{a} is NOT perfect.")
  

