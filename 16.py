pss,spp=map(int,input().split())
lis=list(map(int,input().split()))
if spp==1:
    print(min(lis))
elif spp==2:
    print(max(lis[0],lis[pss-1]))
else:
    print(max(lis))
