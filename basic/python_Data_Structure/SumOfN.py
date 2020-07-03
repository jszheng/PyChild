import time


def sumOfN(n):
    start = time.time()
    Nsum = 0

    for i in range(1, n + 1):
        Nsum = Nsum + i

    end = time.time()

    return Nsum, (end - start)


print(sumOfN(100000))
