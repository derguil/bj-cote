import sys
input=sys.stdin.readline

n=int(input())
lsn=list(map(int, input().split()))
m=int(input())
lsm=list(map(int, input().split()))

lsn.sort()
def binary_search(target, start, end):
    if start > end:		 # 범위를 넘어도 못찾는다면 -1을 반환
        return -1

    mid = (start + end) // 2  # 중간값

    if lsn[mid] == target:	# 중간값의 데이터가 target과 같다면 mid를 반환
        return mid 

    elif lsn[mid] > target: # target이 작으면 왼쪽 탐색
        end = mid - 1
    else:                    # target이 크면 오른쪽 탐색
        start = mid + 1

    return binary_search(target, start, end) # 줄어든 범위를 더 탐색

for i in lsm:
    if(binary_search(i,0,n-1) == -1):  
        print(0)
    else:
        print(1)
