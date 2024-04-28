def read_graph_as_edges_w(n):
    graph = [list(map(int, input().split())) for i in range(n)]
    return graph
def read_graph_as_neigh_matrix_w(n):
    edge_list = read_graph_as_edges_w(n)
    vertex_set = set()
    for edge in edge_list:
        vertex_set.add(edge[0])
        vertex_set.add(edge[1])
    V_num = len(vertex_set)
    res_matrix = [[10**10 for i in range(V_num)] for j in range(V_num)]
    for edge in edge_list:
        index_1 = edge[0] - 1
        index_2 = edge[1] - 1
        res_matrix[index_1][index_2] = edge[2]
    return res_matrix, edge_list

def MST(graph1,graph2,m):
    v = len(graph1)
    visited = []
    for i in range(v):
        for j in range(v):
            if graph1[i].count(min(graph1[i])) == 1 and graph1[i][j] == min(graph1[i]):
                visited.append([i+1,j+1,min(graph1[i])])
                visited.append(['any'])
            elif graph1[i].count(min(graph1[i])) < v and graph1[i][j] == min(graph1[i]):
                visited.append([i+1,j+1,min(graph1[i])])
                visited.append(['at least one'])
    j = 0
    for i in graph2:
        if i not in visited:
            print('none')
        else:
            print(visited[2*j+1][0])
            j+=1
m,n = map(int, input().split())
graph1, graph2 = read_graph_as_neigh_matrix_w(n)
MST(graph1,graph2,n)
"""
4 5
0 1 101
0 2 100
1 2 2
1 3 2
2 3 1
"""
"""
4 5
1 2 101
1 3 100
2 3 2
2 4 2
3 4 1
none
any
at least one
at least one
any
"""