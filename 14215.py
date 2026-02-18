a = list(map(int, input().split()))
a.sort()
if a[2] >= a[0] + a[1]:
    print(2 * (a[0] + a[1]) - 1)
else:
    print(sum(a))
