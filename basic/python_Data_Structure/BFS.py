from collections import deque
# 广度优先算法

def person_is_a_seller(name): # 定义判断函数
    return name[-1] == 'm'


graph = {
         'ME': ['Alice', 'Bob', 'Clair'],
         'Bob': ['Anju', 'Peggy'],
         'Alice': ['Peggy'],
         'Clair': ['Thom', 'Jonny'],
         'Anju': [],
         'Peggy': [],
         'Thom': [],
         'Jonny': []
         } # 创建图


search_queue = deque() # 创建队列
searched = [] # 创建已查找的列表
search_queue += graph['ME'] # 加入自己的邻居

while search_queue: # 当队列人数不为零时
    person = search_queue.popleft() # 弹出第一个对象
    if person not in searched:
        if person_is_a_seller(person):
            print(person)

        else:
            search_queue += graph[person] # 将该对象的邻居加入队列

    else:
        searched.append(person) # 添加该对象