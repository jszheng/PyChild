# 动态规划
tr = [None, {'w': 2, 'v': 3},
      {'w': 3, 'v': 4},
      {'w': 4, 'v': 8},
      {'w': 5, 'v': 8},
      {'w': 9, 'v': 10}]  # w代表重量，v代表价值
# 设置目标的属性
weight_max = 20
# 设置重量上限
m = {(i, w): 0 for i in range(len(tr))
     for w in range(weight_max + 1)}  # i代表取物数量，w代表重量
# 设置元素皆为零的二维表
# 逐次填写二维表
for i in range(1, len(tr)):  # 外层循环遍历所有的取法数量
    for j in range(1, weight_max + 1):  # 内层循环遍历其重量
        if int(tr[i]['w']) > j:
            m[(i, j)] = m[(i - 1, j)]  # 超出重量极限则不加入 继承之前的取法

        else:
            m[(i, j)] = max(m[(i - 1, j)],
                            m[i - 1, j - tr[i]['w']] + tr[i]['v'])

print(m[5, 20])