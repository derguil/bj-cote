import sys
input=sys.stdin.readline

def can(n):
    if n == 1:
        return ["*"]

    prev = can(n // 3)
    result = []

    for row in prev:
        result.append(row * 3)

    for row in prev:
        result.append(row + " " * (n // 3) + row)

    for row in prev:
        result.append(row * 3)

    return result


n = int(input())
print("\n".join(can(n)))