 
input()
lis= [int(i) for i in input().split()]
temp = []
for i in lis:
    if i not in temp:
        temp.append(i)
temp = sorted(temp)
print (temp[-2])