a=int(input())
b=0

for i in range(0,a):
  c=input()
  t=[c[0]]
  for j in range(1,len(c)):
    if (c[j-1] != c[j]):
      t.append(c[j])
  if(len(set(t)) == len(t)):
    b+=1
print(b)



               