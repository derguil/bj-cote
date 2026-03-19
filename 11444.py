import sys
input = sys.stdin.readline

MOD = 1000000007

def mul(a, b):
    return [
        [(a[0][0]*b[0][0] + a[0][1]*b[1][0]) % MOD,
         (a[0][0]*b[0][1] + a[0][1]*b[1][1]) % MOD],

        [(a[1][0]*b[0][0] + a[1][1]*b[1][0]) % MOD,
         (a[1][0]*b[0][1] + a[1][1]*b[1][1]) % MOD]
    ]

def power(mat, n):
    if n == 1:
        return mat

    half = power(mat, n//2)

    if n % 2 == 0:
        return mul(half, half)
    else:
        return mul(mul(half, half), mat)

n = int(input())

if n == 1:
    print(1)
else:
    base = [[1,1],[1,0]]
    res = power(base, n-1)
    print(res[0][0])