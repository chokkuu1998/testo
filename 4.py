AAA=int(input())
bbb=str(A)
kkk=[]
sss=[]
sum=0
for i in range(0,len(bbb)):
    sss.append(bbb[i])
kkk=list(map(int,sss))
if len(kkk)==1:
    print(kkk[0]**2)
else:
    for i in range(0,len(kkk)-1):
        sum=sum+(kkk[i]**kkk[i+1])
    else:
        sum=sum+(kkk[-1]**kkk[0])
    print(sum)
