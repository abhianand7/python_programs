 
input()
first_set = set((int(i) for i in input().split()))
input()
second_set = set((int(i) for i in input().split()))

for i in sorted(first_set.symmetric_difference(second_set)):
    print (i)
