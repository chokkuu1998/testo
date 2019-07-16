xx,yy=input().strip().split(" ")
yy=int(yy)
sum=0
while(sum<len(xx)-1 and yy):
  if(x[sum]>x[sum+1]):
    yy-=1
    xx=xx[:sum]+x[sum+1:]
    if(sum!=0):
      sum-=1
  else:
    sum+=1
q1=x[:len(xx)-yy]
print(q1)
