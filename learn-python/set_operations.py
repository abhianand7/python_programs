# set operations

set_data = set()
# add operation

set_data.add('a')       # if a already exits nothing happens
print (set_data)

# update operation

set_data.update({1,2,3})
print (set_data)

set_data.update([1,4,5])
print(set_data)

set_data.update((1,2,3))
print(set_data)

# remove operation - discard() and remove() both takes a single value

set_data.discard(1)     # discard does nothing if the value is not present in set
print (set_data)

set_data.remove(2)      # remove raises an key error exception if value is not present
print(set_data)

# Common Set operations
another_set = {1,2,3,4,5,6,9,10}

print (set_data.intersection(another_set))  # values which are present in both
print("set_data = " , set_data, sep = '')

print (set_data.difference(another_set))    # unique elements in set_data
print("set_data = " , set_data, sep = '')

print (set_data.symmetric_difference(another_set))  # unique elements of both the sets
print("set_data = " , set_data, sep = '')

print (set_data.union(another_set))         # union of set_data and another_set
print("set_data = " , set_data, sep = '')

a = {'a',1,5,'c', 'b', 3, 2, 'f', 'd'}
b = {'z', 'a', 2, 'c', 13, 10, 'd', 22}

a.difference_update(b)
print (a)

a = {'a',1,5,'c', 'b', 3, 2, 'f', 'd'}
b = {'z', 'a', 2, 'c', 13, 10, 'd', 22}

a.intersection_update(b)
print(a)

a = {'a',1,5,'c', 'b', 3, 2, 'f', 'd'}
b = {'z', 'a', 2, 'c', 13, 10, 'd', 22}

a.symmetric_difference_update(b)            # this is nothing but the union of a.intersection(b) and b.intersection(a)

print (a)
