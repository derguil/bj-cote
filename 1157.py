a=input().upper()
b={}
for i in a:
    if(i in b):
        b[i] += 1
    else:
        b[i] = 1
bestC=None
best=0
dup=False

for i, j in b.items():
    if j > best:
        best = j
        bestC = i
        dup = False
    elif j == best:
        dup = True

if(dup):
    print("?")
else:
    print(bestC)


