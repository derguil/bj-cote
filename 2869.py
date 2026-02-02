import math
u,d,v=map(int,input().split())
print(math.ceil((v-u)/(u-d)) + 1)