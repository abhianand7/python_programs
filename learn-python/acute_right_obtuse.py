
#!/bin/python3

import sys
import itertools
import math
def iftriangle(a):
    large = {max(a)}
    other_sides = list(set.difference(set(a), large))
    large = list(large)
    if ((large[0]+ other_sides[0]) > other_sides[1]) and((large[0] + other_sides[1]) > other_sides[0] and sum(other_sides) > large[0]) :
        return True
    else :
        return False
def angle (a, b, c):
    return math.degrees(math.acos((c**2 - b**2 - a**2)/(-2.0 * a * b)))
N = int(input().strip())
A = [int(A_temp) for A_temp in input().strip().split(' ')]
# your code goes here
L = list(itertools.combinations(A,3))
acute,right,obtuse = 0,0,0
for i in L:
    if iftriangle(i):
        a = i[0]
        b = i[1]
        c = i[2]
        angA = angle(a,b,c)
        angB = angle(b,c,a)
        angC = angle(c,a,b)
        if angA < 90 and angB < 90 and angC < 90:
            acute += 1
        elif angA == 90 or angB == 90 or angC == 90:
            right += 1
        elif angA > 90 or angB > 90 or angC > 90 :
            obtuse += 1
print (acute,right,obtuse)