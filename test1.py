# my first python script

import sys
print(sys.platform)
print(2**100)
x = 'spam!'
print(x*8)


import math
print math.pi

import random
print random.random()

print x[1:3] # not include [3]

str = "aaaa,bbbb,ccccc"
print str
print str.split(',')

print '%s egg, %s pot' % ('spam', 'max')

D = {'k1':'v1', 'k2':'v2'}
print D['k1']
print D.keys()
print 'k1' in D
print 'no' in D

#for c in "hacker" : print(c, end=' ')
