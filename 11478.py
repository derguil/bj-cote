a=input()
b=set()
for i in range(len(a)):
  for j in range(i+1,len(a)+1):
    b.add(a[i:j])
print(len(b))