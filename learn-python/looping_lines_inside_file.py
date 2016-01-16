fobj = open("D:\\PyScripter-v2.6.0\PyScripter\output.txt","r")
for x in fobj:
    print(x,end = 'w')
    for i in x:
        print(i)
   # print(type(x))