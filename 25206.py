pdic = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0
}
b=0
c=0
for i in range(20):
  a=input().split()
  if a[2]!="P":
    c+=float(a[1])
    b+=float(a[1])*pdic[a[2]]
print(b/c)

