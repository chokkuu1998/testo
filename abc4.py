uu=input()
oo=len(uu)
cc=[]
for y in range(0,oo,2):
    cc.append(uu[y:y+2][::-1])
print(''.join(cc))
