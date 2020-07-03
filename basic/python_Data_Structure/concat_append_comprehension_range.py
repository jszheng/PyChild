import timeit

def list_1():
    l1 = []
    for i in range(1000):
        l1 = l1 + [i]

    return l1


def list_2():
    l2 = []
    for i in range(1000):
        l2.append(i)

    return l2


def list_3():
    l3 = [i for i in range(1000)]

    return l3


def list_4():
    l4 = list(range(1000))

    return l4


if __name__ ==  '__main__':
    t1 = timeit.timeit(stmt=(list_1), number=1000)
    print(t1)

    t2 = timeit.timeit(stmt=(list_2), number=1000)
    print(t2)

    t3 = timeit.timeit(stmt=(list_3), number=1000)
    print(t3)

    t4 = timeit.timeit(stmt=(list_4), number=1000)
    print(t4)

