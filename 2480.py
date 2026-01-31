a,b,c = map(int,input().split())
d = 0
e = {a,b,c}
if len(e) == 1:
    d = 10000+a*1000

if len(e) == 2:
    g = [a,b,c]
    for k in e:
        g.remove(k)
    g = g[0]
    d = 1000+g*100

if len(e) == 3:
    d = max(a,b,c)*100

print(d)