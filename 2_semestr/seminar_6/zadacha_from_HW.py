def read_graph_as_edges_w():
    n = int(input())
    graph = [list(map(int, input().split())) for i in range(n)]
    # for i in range(n):
    #     graph.append(list(map(int, input().split())))
    return  graph
def read_graph_as_neigh_list_w():
    edge_list = read_graph_as_edges_w()
    graph_dict = {}  # dict()
    vertex_set = set()
    for edge in edge_list:
        vertex_set.add(edge[0])
        vertex_set.add(edge[1])
    for v in vertex_set:
        graph_dict[v] = frozenset()
    for edge in edge_list:
            graph_dict[edge[0]] = graph_dict[edge[0]] | frozenset([(edge[1],edge[2])])
    return graph_dict
def read_graph_as_neigh_matrix_w():
    edge_list = read_graph_as_edges_w()
    vertex_set = set()
    for edge in edge_list:
        vertex_set.add(edge[0])
        vertex_set.add(edge[1])
    V_num = len(vertex_set)

    res_matrix = [[0 for i in range(V_num)] for j in range(V_num)]
    for edge in edge_list:
        index_1 = edge[0] - 1
        index_2 = edge[1] - 1
        res_matrix[index_1][index_2] = edge[2]

    return res_matrix
def print_matrix_w(matrix):
    for line in matrix:
        print(*line)
def Dijkstra_sum_min(graph, v):
    d = {}
    visited = []
    end = []
    for key in graph.keys():
        d[key] = float('infinity')

    d[v] = 0
    visited.append([0, v])
    while visited:
        visited.sort()

        c = visited.pop(0)
        end.append(c[1])
        for neigh in graph[c[1]]:
            if neigh[0] not in end:
                if (d[c[1]] + neigh[1]) < d[neigh[0]]:
                    d[neigh[0]] = (d[c[1]] + neigh[1])
                visited.append(neigh[::-1])
            if d[neigh[0]] < 0:
                return False

    return True

graph = read_graph_as_neigh_list_w()
print(Dijkstra_sum_min(graph, 1))


"""
3
2 4 3
<=
1 5 7
>=
3 4 2 
<=
"""

"""
3 
2 4 3
1 5 7
3 4 2
"""

"""
3
2 1 3
2 3 2
1 3 7
"""

'''
4
2 4 3
<=
6 7 8 
<=
5 9 4
<=
7 8 9
<=
'''