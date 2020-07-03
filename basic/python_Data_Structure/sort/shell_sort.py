def shellsort(alist):
    gap = len(alist)//2
    n = len(alist)

    while gap > 0:
        for i in range(gap):

            for index in range(i+gap, n, gap):
                position = index
                currentvalue = alist[index]

                while position > 0 and alist[position-gap] > currentvalue:
                    alist[position] = alist[position-1]
                    position = position -1

                alist[position] = currentvalue

        gap //= 2


test_list = [2, 6, 4, 8, 5, 1]
shellsort(test_list)
print(test_list)


