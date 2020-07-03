import time,timeit


def sumofN_1(n):
    start = time.time()
    num = 0
    for i in range(1, n+1):
        num = num + i

    end = time.time()

    return num, end-start


print(sumofN_1(100))


def sumofN_2(n):
    return (n*(n+1))/2


print(sumofN_2(10))
