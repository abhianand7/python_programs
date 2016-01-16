 
S = input()

from collections import OrderedDict
T = ''.join(OrderedDict.fromkeys(S))
#from operator import itemgetter
tuple_list = []
#print (T)
count = 0
for i in T:
    tuple_list[len(tuple_list):] = [(i,S.count(i))]
    
X= sorted(tuple_list,reverse = True, key = lambda x:x[1])

#print (X)
print (X[0][0], X[0][1])
print (X[1][0], X[1][1])
print (X[2][0], X[2][1])
    