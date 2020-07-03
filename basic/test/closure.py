#!/usr/bin/env python3

def make_counter(x):
    print('entering make_counter')
    while True:
        yield x
        print('increment x')
        x = x + 1


counter = make_counter(2)

counter
next(counter)

next(counter)

def fib(max):
    a, b = 0, 1
    while a<max :
        yield a
        a, b = b, a+b


for n in fib(1000):
    print(n)