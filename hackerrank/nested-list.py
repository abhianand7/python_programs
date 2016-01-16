 
all_students = []
for i in range(int(input())):
    all_students.append([input(), float(input())])
from operator import itemgetter
#print (all_students)
all_students = sorted(all_students, key = itemgetter(1,0))
#print (all_students)
new_lis = []
if len(all_students) > 1:
    for i in all_students:
        new_lis.append(i[1])
    unique = []
    for i in new_lis:
        if i not in unique:
            unique.append(i)
    if len(unique) > 1:
        lowest_second = unique[1]
    for i in all_students:
        if i[1] == lowest_second:
            print (i[0])

