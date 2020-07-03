def bubble_sort(alist):
    exchange = True
    passnum = len(alist) - 1

    while passnum > 0 and exchange:
        exchange = False

        for i in range(passnum):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]

        passnum = passnum - 1


alist=[20,30,40,90,50,60,70,80,100,110]
bubble_sort(alist)
print(alist)

'''
def bubblesort(a_list):
    move = 1

    while move != 0 is True:
        move = 0

        for i in range(len(a_list)-1):
            if a_list[i] > a_list[i+1]:
                a_list[i], a_list[i+1] = a_list[i+1], a_list[i]

                move = move + 1



alist = [20,30,40,90,50,60,70,80,100,110]
bubblesort(alist)
print(alist)
'''


