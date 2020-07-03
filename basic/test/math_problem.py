
set_A = [2, 4, 6, 8, 10]
set_B = [1, 2, 4, 8, 16]
intersection = []
def inter():
    for ele_A in set_A:
        if ele_A in set_B:
            intersection.append(ele_A)



    for i in intersection:
        print(i)


print(inter())