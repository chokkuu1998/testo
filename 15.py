ttt1,ttt2=map(int,input().split())
li=list(map(int,input().split()))
if ttt2==1:
  print(min(li))
elif ttt2==2:
  print(max(li[0],li[ttt1-1]))
else:
  print(max(li))
