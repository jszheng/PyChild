#!/usr/bin/env python3

class Fib:
    '''ffibs'''

    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib


fib = Fib(100)
print(fib)
print(fib.__class__)
print(fib.__doc__)

for n in Fib(1000):
    print (n, end=' ')