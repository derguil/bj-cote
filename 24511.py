n=int(input())
qs=list(map(int, input().split()))
fir=list(map(int, input().split()))
inpn=int(input())
inp=list(map(int, input().split()))

print(*([fir[i] for i in range(n) if qs[i]==0][::-1]+inp)[:inpn])