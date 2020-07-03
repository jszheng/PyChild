def SelectSort(alist):

    for i in range(len(alist) - 1, -1, -1):
        for j in range(0, i):
            if alist[j] > alist[i]:
                alist[i], alist[j] = alist[j], alist[i]

    return alist

print(SelectSort([2, 5, 6, 3, 4]))
                