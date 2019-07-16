a=int(input())
b=list(map(str,input().split()))[:a]
l=[]
t=[]
for i in range(0,len(b)):
    l.append(b[i].lower())
for i in range(0,a):
      m=min(l)
      t.append(m)
      l.remove(min(l))
for i in t:
    print(i)
