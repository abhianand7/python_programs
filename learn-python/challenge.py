x = [i for i in input().split()]
elements = [i for i in input().split()]
final = []
greater = []
def result(query,elements):
    greater = [i for i in elements if i>=query[0]]
    #print (greater)
    final.append(greater[(int(query[1]) -1)])
for i in range(int(x[1])):
    query = [i for i in input().split()]
    result(query,elements)

for i in final:
    print(int(i))

