def read_graph_as_edges():
    d,n = list(map(int, input().split()))
    graph = [list(map(int, input().split())) for i in range(n)]
    # for i in range(n):
    #     graph.append(list(map(int, input().split())))
    return  graph
def read_graph_as_neigh_matrix():
    edge_list = read_graph_as_edges()
    vertex_set = set()
    for edge in edge_list:
        vertex_set.add(edge[0])
        vertex_set.add(edge[1])
    V_num = len(vertex_set)
    res_matrix = [[0 for i in range(V_num)] for j in range(V_num)]
    for edge in edge_list:
        index_1 = edge[0] - 1
        index_2 = edge[1] - 1
        res_matrix[index_1][index_2] = 1

    return res_matrix

graph = read_graph_as_neigh_matrix()
b = len(graph[0])
a = -1
d = -1
Flag = True
for i in graph:
    a += 1
    d = 0
    for v in i:
        if v == graph[d][a] and d!=a and Flag:
            print('no')
            Flag = False
        d+=1
if Flag:
    print('yes')
"""
4 6
1 2
1 3
4 1
2 3
4 2
4 3 
"""
"""
4 5 
1 2
1 3
2 3
4 2
4 3
"""
"""
4 7
1 2
1 3
4 1
2 3
4 2
4 3
1 4
"""