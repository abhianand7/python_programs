# float formatting

a = 12.53524
# Method 1

print (float("%.2f" % a))               # without float it will return string

# Method 2

print (float("{0:.2f}".format(a)))      # without float it will return string

# Method 3

print (float(format(a, ".2f")))         # without float it will return string

# Method 4

print ((round(a,2)))

# Method 5

from decimal import Decimal

print (type(Decimal(a)))
