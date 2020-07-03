
set_A = [2, 4, 6, 8, 10]
set_B = [1, 2, 4, 8, 16]
union = []

for ele_B in set_B:
    union.append(ele_B)
for ele_A in set_A:
    if ele_A not in set_B:
        union.append(ele_A)


for union_ele in union:
    print(union_ele)



