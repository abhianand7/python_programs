 
# Enter your code here. Read input from STDIN. Print output to STDOUT
AB = int(raw_input())
BC = int(raw_input())
import math
AC = math.sqrt(AB**2 + BC**2)

if float(AB+BC) > AC:
    MC = AC/2
    MBC = MC/BC
    Angle = int(round(math.degrees(math.acos(MBC))))
    print "%s°"%(Angle)
else :  print 0