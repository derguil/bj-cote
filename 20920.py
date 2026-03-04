import sys
input=sys.stdin.readline

a,b=map(int,input().split())
words={}
for _ in range(a):
  word=input().strip()
  if(len(word)<b):
    continue
  else:
    if word in words:
      words[word]+=1
    else:
      words[word]=1

sorted_words=sorted(words, key=lambda x:(-words[x], -len(x), x))
print("\n".join(sorted_words)) 