a = input()
arr = []

for i in range(26):
    pos = -1
    for j in range(len(a)):
        if chr(i + 97) == a[j]:
            pos = j
            break
    arr.append(pos)

print(*arr)
