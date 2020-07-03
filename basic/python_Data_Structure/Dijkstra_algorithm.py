# 狄克斯特拉算法
graph = {}
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2
graph['a'] = {}
graph['a']['fin'] = 1
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5
graph['fin'] = {} # 创建图的散列表

infinity = float('inf')
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity # 创建开销表

parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None # 创建父节点表

processed = [] # 处理过的节点


def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None

    for node in costs: # 遍历所有节点
        cost = costs[node]
        if cost < lowest_cost and node not in processed: # 开销更低且未被处理过
            lowest_cost = cost # 视其为开销最小的节点
            lowest_cost_node = node

    return lowest_cost_node


node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]

    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node

    processed.append(node)
    node = find_lowest_cost_node(costs)

print(costs)




