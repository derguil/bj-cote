c=[]
for _ in range(5):
  c.append(list(input()))
a=len(max(c, key=len))
for i in range(5):
  if(len(c[i]) < a):
    c[i].extend("*" * (a - len(c[i])))

d=[]

for i in range(a):
  for j in range(5):
    if(c[j][i] != "*"):
      d.append(c[j][i])

print("".join(d))
