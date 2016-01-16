 
x = int(input())
y = int(input())
z = int(input())
N = int(input())

import itertools
all_sets = [list(i) for i in (itertools.product(range(x+1),repeat = 3)) if sum(i) != N]
print (all_sets)
