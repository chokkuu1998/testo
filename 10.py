ww=int(input())
ss=0
mm=len(str(ww))
while ww>0:
    a=int(ww)%10
    ss=ss+(a**mm)
    ww=ww//10
print(ss)
