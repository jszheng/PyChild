def Seqencesearch(target, alist):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        temp = alist[pos]
        if temp == target:
            found = True

        else:
            pos = pos + 1

    return found


testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(Seqencesearch(3, testlist))
print(Seqencesearch(13, testlist))
