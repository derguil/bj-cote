x, y, w, h = map(int, input().split())

print(min(min(y,h-y),min(x,w-x)))