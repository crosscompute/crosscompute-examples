# http://stackoverflow.com/questions/16007204/factorizing-a-number-in-python
import sys
from math import sqrt


integer = int(sys.argv[1])
minimum_factor = 2
factors = []
while integer > 1:
    for i in xrange(minimum_factor, int(sqrt(integer + 0.05)) + 1):
        if integer % i == 0:
            integer /= i
            minimum_factor = i
            factors.append(i)
            break
    else:
        if integer > 1:
            factors.append(integer)
            break
print('factors = %s' % factors)
print('unique_factor_count = %s' % len(set(factors)))
