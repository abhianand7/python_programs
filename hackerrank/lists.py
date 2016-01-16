 
L = []

for i in range(int(input())):
    temp = input().split()
    if temp[0] == "insert":
        L.insert(int(temp[1]),int(temp[2]))
    elif temp[0] == "append":
        L.append(int(temp[1]))
    elif temp[0] == "remove":
        L.remove(int(temp[1]))
    elif temp[0] == "pop":
        L.pop()
    elif temp[0] == "print":
        print(L)
    elif temp[0] == "index":
        L.index(int(temp[1]))
    elif temp[0] == "reverse":
        L.reverse()
    elif temp[0] == "sort":
        L.sort()
        