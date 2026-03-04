import sys
input=sys.stdin.readline

n = int(input())
nums=list(map(int,input().split()))
ls=list(map(int,input().split()))
abcd=[]
res=[]

def dfs(abcd,ls):
  if(len(abcd)==n-1):
    result=nums[0]
    for i in range(1,n):
      if(abcd[i-1]==0):
        result+=nums[i]
      elif(abcd[i-1]==1):
        result-=nums[i]
      elif(abcd[i-1]==2):
        result*=nums[i]
      elif(abcd[i-1]==3):
        result=int(result/nums[i])
    res.append(result)
    return

  for i in range(4):
    if(ls[i]>0):
      ls[i]-=1
      abcd.append(i)
      dfs(abcd,ls)
      abcd.pop()
      ls[i]+=1
      
dfs(abcd,ls)

print(max(res))
print(min(res))