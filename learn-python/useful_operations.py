# Some Important and useful operations and keywords

# 1.

print (hasattr(list, "append"))       # This gives a bool value of the object whether it has the specified attribute or not

print(hasattr(dict,"append"))

# 2.

print (hash((1,2,3)))           # calculates the hash of the object

""" hash can be calculated for tuple but not for list since tuple is immutable
and list is mutable"""

# 3.

# converting the int in a list which is currently is in str form

lis = ['1', '2', '3', '4']

newlis = list(map(int,lis))
print (newlis)

# 4.

tuple([1,2,3])          # creating tuple from a list
list((1,2,3))           # creating list from a tuple
set([1,2,4])            # creating set from a list                                  Remember that set always creates an asceding order of data and removes the dupkicates from the object
set((1,2,3))            # creating set from a tuple
list({1,2,3})           # creating list from a set
tuple({1,2,3})          # creating tuple from a set

# 5.

list.__dict__.keys()    # to see all the attributes of a class(relpce list with any other object name)
dir(list)               # returns the attributes in the form of list of strings

# 6.

hasattr(set, "__iter__")        # to check if a paticular object has a particular attribute or not, here it is checked whether set is iterable or not

# 7.
""" Important Note - whenever trying to search anything from a data always try to use set as in general when you perform a search python compares
it to every other values untill it finds one but in case of set it keeps track of its data using hash table so when you try to search it just looks up the
hash value of that data or object and return the result fairly quickly thus reducing the time complexity of the operation"""


# 7.
