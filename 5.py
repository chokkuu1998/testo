nn=input()
ss=j=0
for i in range(0,len(nn)):
    j=j+1
    if len(nn) == 1:
        ss = ss + (int(nn[i]) ** (j + 1))
    elif i==len(nn)-1:
        ss=ss+int(nn[i])
    else: ss=ss+(int(nn[i])**(j+1))
print(ss)
