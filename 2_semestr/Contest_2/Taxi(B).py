"""
Алгоритм Диикстры
Перевести км в стоимость
"""
n, A, B, C, d = map(float, input().split())
m = int(input())
def read_graph_as_neigh_list_w():
    edge_list = road
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
def Dijkstra_sum_min(graph, v, u):
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

    return d[u]
road = []
for i in range(m):
    dfr = list(map(float, input().split()))
    road.append(dfr)
    dft = [dfr[1], dfr[0], dfr[-1]]
    road.append(dft)
graph = read_graph_as_neigh_list_w()
road = [Dijkstra_sum_min(graph, A, B),Dijkstra_sum_min(graph,B,C), Dijkstra_sum_min(graph,A, C)]
print((road[0]+road[1]-road[2])*d)
"""
5 1 2 3 4.25
5
1 4 2.5
4 2 3
4 5 3
3 5 2
3 4 8
"""