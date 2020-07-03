__author__ = 'jszheng'


import math

def rbv(v, n):
    r = 0
    for i in range(n):
        r |= (v >> n-i-1 & 1) << i
    return r

def demort(v, n):
    d = 0
    for i in range(n):
        d |= (v & (1 << (i<<1))) >> i
    return d

# demort
a = 4039
w = 6
b = demort(a, w)
print("demort(7, 6)=", b)
b = demort(a>>1, w)
print("demort(7>>1, 6)=", b)

