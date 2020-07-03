def binarysearch(alist, target):
    if len(alist) == 0:
        return False

    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == target:
            return True
        else:
            if target < alist[midpoint]:
                return binarysearch(alist[0:midpoint], target)

            else:
                return binarysearch(alist[midpoint + 1:], target)


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binarysearch(testlist, 3))
print(binarysearch(testlist, 13))
