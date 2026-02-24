c=[0]*10001
len = int(input())
for _ in range(len):
  i = int(input())
  c[i] += 1

result = []
for i in range(len):
    result += [i] * c[i]

print(*result, sep="\n")