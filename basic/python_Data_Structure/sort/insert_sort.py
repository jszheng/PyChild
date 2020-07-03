def insertsort(alist):
    for index in range(1, len(alist)):
        currentvalue = alist[index]
        position = index

        while position > 0 and alist[position - 1] > currentvalue:
            alist[position] = alist[position-1]
            position = position-1

        alist[position] = currentvalue


a_list = [54,26,93,17,77,31,44,55,20]
insertsort(a_list)
print(a_list)


def insertsort_reversetype(alist):
    for j in range(1, len(alist)):
        key = alist[j]
        while key > alist[j-1] and j > 0:
            alist[j] = alist[j-1]
            alist[j-1] = key
            j = j - 1


a_list = [54,26,93,17,77,31,44,55,20]
insertsort_reversetype(a_list)
print(a_list)

a_listtest = [1, 2, 3, 4, 5]
insertsort_reversetype(a_listtest)
print(a_listtest)