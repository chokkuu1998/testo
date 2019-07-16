NN = int(input())
SS= list(input().split())
AA = []
for i in SS:
  if int(i)==78 or int(i)==1 or int(i)==4:
    AA.append('+')
  elif int(i[-2:])==35:
    AA.append('-')
  elif int(i[0])==9 and int(i[len(i)-1])==4:
    AA.append('*')
  elif int(i[:3])==190:
    AA.append('?')
  else:
    AA.append('*')
for i in AA:
  print(i)
