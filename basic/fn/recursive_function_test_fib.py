def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


while True:
    n = int(input('fib_num: '))
    print(fib(n))





