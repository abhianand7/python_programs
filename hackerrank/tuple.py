 
N = int(input())

l = (int(i) for i in input().split())
l = tuple(l)
print (hash(l))
