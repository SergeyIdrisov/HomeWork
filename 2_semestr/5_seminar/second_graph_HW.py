def read_graph_as_edges_w():
    n = int(input())
    graph = [list(map(int, input().split())) for i in range(n)]
    # for i in range(n):
    #     graph.append(list(map(int, input().split())))
    return graph
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
def DFS_w(graph, v, visited=[]):
    # print(v)
    visited.append(v)
    for neigh in graph[v]:
        if neigh not in visited:
            DFS_w(graph, neigh, visited)
def isCyclicUtil(v, visited, recStack, graph):
    visited[v] = True
    recStack[v] = True

    for neighbour in graph[v]:
        if visited[neighbour[0]] == False:
            if isCyclicUtil(neighbour[0], visited, recStack, graph) == True:
                return True
        elif recStack[neighbour[0]] == True:
            return True

    # The node needs to be popped from
    # recursion stack before function ends
    recStack[v] = False
    return False
def has_cycle_w(graph):
    V=len(graph)
    visited = [False] * (V + 2)
    recStack = [False] * (V + 2)
    for node in range(V):
        if visited[node] == False:
            if isCyclicUtil(node+1, visited, recStack, graph) == True:
                return True
    return False
def topologicalSortUtil_w(graph, v, visited, stack=[], i=1):
    visited[v] = True
    for v in graph:
        if visited[i] == False:
            topologicalSortUtil_w(graph, i, visited, stack)
            stack.append(v)
        i += 1
def topologicalSort_w(graph):
    if has_cycle_w(graph) == False:
        visited = [False] * (len(graph) + 1)
        stack = []
        for i in range(len(graph)):
            if visited[i] == False:
                topologicalSortUtil_w(graph, i, visited, stack)
        return stack
    else:
        t = 'Невозможно выполнить из-за присутсвия цикла в данном графе...'
        return t
def road_in_v_from_u_w(graph, v, u):
    Topolog_list = topologicalSort_w(graph)
    if type(Topolog_list) == str:
        return Topolog_list
    else:
        tops = {v: 0 for v in graph}
        tops[v] = 1
        for i in Topolog_list[::-1]:
            for j in graph[i]:
                tops[j] += tops[i]
        # {1:1, 2:0, 3:0, 4:0} -> {}
        # {1: frozenset({2, 3}), 2: frozenset({4}), 3: frozenset({4}), 4: frozenset()}
        # [4,3,2,1]
        return tops[u]
def father_n_w(graph, v, u):
    result = road_in_v_from_u_w(graph, v, u)
    if result > 0:
        return True
    else:
        return False
def bfs_w(graph, v):
    visited = []
    queue = []
    d = {}
    for keys in graph.keys():
        d[keys] = float('infinity')
    visited.append(v)
    queue.append(v)
    d[v] = 0

    while queue:
        u = queue.pop(0)
        print(u, end=" ")

        for neighdour in graph[u]:
            if neighdour not in visited:
                visited.append(neighdour)
                queue.append(neighdour)
                d[neighdour] = d[u] + 1
    return d
def Dijkstra_string_concatenation(graph, v):
    strok = {}
    Dijkstra = Dijkstra_sum_min(graph, v)
    visited = []
    end = []
    for key in graph.keys():
        strok[key] = ''
    Dijkstra[v] = 0
    visited.append([0, v])
    while visited:
        visited.sort()
        c = visited.pop(0)
        end.append(c[1])
        for neigh in graph[c[1]]:
            if neigh[0] not in end:
                if Dijkstra[neigh[0]] >= neigh[1]:
                    strok[neigh[0]]=strok[c[1]]+str(neigh[1])
                visited.append(neigh[::-1])
    return strok
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

    return d
def Dijkstra_sum_max(graph, v):
    d = {}
    visited = []
    end = []
    for key in graph.keys():
        d[key] = 0

    d[v] = 0
    visited.append([0, v])
    while visited:
        visited.sort()

        c = visited.pop(0)
        end.append(c[1])
        for neigh in graph[c[1]]:
            if neigh[0] not in end:
                if (d[c[1]] + neigh[1]) >= d[neigh[0]]:
                    d[neigh[0]] += (d[c[1]] + neigh[1])
                visited.append(neigh[::-1])

    return d
def Dijkstra_mult_min(graph, v):
    d = {}
    visited = []
    end = []
    for key in graph.keys():
        d[key] = float('infinity')

    d[v] = 1
    visited.append([0, v])
    while visited:
        visited.sort()

        c = visited.pop(0)
        end.append(c[1])
        for neigh in graph[c[1]]:
            if neigh[0] not in end:
                if (d[c[1]] + neigh[1]) < d[neigh[0]]:
                    d[neigh[0]] = (d[c[1]] * neigh[1])
                visited.append(neigh[::-1])

    return d
def Dijkstra_color(graph, v):
    d = {}
    colors = {}
    visited = []
    end = []
    for key in graph.keys():
        d[key] = float('infinity')
        colors[key] = float('infinity')
    a = 0
    d[v] = 0
    colors[v] = 0
    visited.append([0, 0, v])  # 1-е число - была ли смена цвета, 2-е - вес, 3-е - вершина
    while visited:
        visited.sort()
        c = visited.pop(0)
        end.append(c[2])
        for neigh in graph[c[2]]:
            list_c = list(list(graph[c[2]])[0])
            if neigh[1] not in end:
                if list_c[0] == neigh[2]:
                    colors[neigh[1]] = colors[c[2]]
                    if (d[c[2]] + neigh[3]) < d[neigh[1]]:
                        d[neigh[1]] = (d[c[2]] + neigh[3])
                    add_visited = [colors[neigh[1]], neigh[3], neigh[1]]
                    visited.append(add_visited)
                else:
                    if colors[neigh[1]] == float('inf'):
                        colors[neigh[1]] = colors[c[2]] + 1
                        if (d[c[2]] + neigh[3]) < d[neigh[1]]:
                            d[neigh[1]] = (d[c[2]] + neigh[3])
                    if colors[neigh[1]] <= colors[c[2]]:
                        continue
                    add_visited = [colors[neigh[1]], neigh[3], neigh[1]]
                    visited.append(add_visited)

    return d, colors
def Floyd_Warshall(graph):
        v = len(graph)
        d = [[float('infinity') for i in range(v)] for j in range(v)]
        nxt = [[-1 for i in range(v)] for j in range(v)]
        for i in range(v):
            for j in range(v):
                if graph[i][j] != 0:
                    d[i][j] = graph[i][j]
                    nxt[i][j] = j
        for k in range(1, v):
            for i in range(v):
                for j in range(v):
                    if d[i][k] + d[k][j] < d[i][j]:
                        d[i][j] = d[i][k] + d[k][j]
                        nxt[i][j] = nxt[i][k]
        return d, nxt
def pth(i, j, nxt):
    p = [i]
    while nxt[i-1][j-1]+1 != j:
        i = nxt[i-1][j-1]+1
        p.append(i)
    p.append(j)
    return p
def bellman_ford(graph, v):
    N = len(graph)
    distance = [[float('infinity')]*N for _ in range(N) ]
    distance[0][v-1] = 0
    for k in range(1,N):
        for i in range(N):
            distance[k][i] = distance[k - 1][i]
            for j in range(N):
                if distance[k - 1][j] + graph[j][i] < distance[k][i] and graph[j][i]!=0:
                    distance[k][i] = distance[k - 1][j] + graph[j][i]
    return distance[-1]
def kruskal(graph): # read_graph_as_edges
    g = graph
    for e in g:
        e[0], e[2] = e[2], e[0]
    g.sort()
    tree_v = set()
    tree_e = []
    for e in g:
        if e[1] not in tree_v or e[2] not in tree_v:
            tree_v.add(e[1])
            tree_v.add(e[2])
            tree_e.append(e)
        else:
            continue
    return tree_e
from heapq import *
def prim(graph):  # read_graph_as_neigh_list_w
    v = 1
    tmp = list(graph[v])
    h = []
    for e in tmp:
        h.append([e[1], e[0], v])
    heapify(h)
    tree_v = set([v])
    tree_e = []
    while h:
        e_min = heappop(h)
        if e_min[1] not in tree_v:
            tree_v.add(e_min[1])
            for e in graph[e_min[1]]:
                t = [e[1], e[0]]
                heappush(h, (list(t) + [e_min[1]]))
            v = e_min[1]
            tree_e.append(e_min)
        else:
            continue
    return tree_e


graph1 = read_graph_as_neigh_list_w()
#graph2 = read_graph_as_neigh_matrix_w()
#DFS_w(graph, 1)
# print(has_cycle(graph1, 1))
#print(topologicalSort_w(graph1))
#print(graph1)
#print(graph2)
#print_matrix_w(read_graph_as_neigh_matrix_w())
# print(road_in_v_from_u(graph1, 7, 6))
# print(father_n(graph1, 6 , 7))
#d = bfs_w(graph1, 1)
#print(d)
#print(Dijkstra_sum_min(graph1, 1))
#print(Dijkstra_sum_max(graph1, 1))
#print(Dijkstra_mult_min(graph1, 1))
#print(Dijkstra_string_concatenation(graph1, 1))
#D, P = Floyd_Warshall(graph2)
#print(D)
#print(P)
#print(pth(1, 3, P))
#print(bellman_ford(graph2, 1))
#print(kruskal(graph1))
print(prim(graph1))
'''
8
1 4 6
1 2 1
3 2 2
2 5 3
2 6 1
5 3 1
6 2 2
6 4 1
'''
'''
10
1 2 3
1 3 6
2 4 2
2 5 5 
3 4 7
4 5 1
5 6 8 
4 6 11
3 7 9
7 6 10
'''
'''
5
1 2 1
2 4 1
4 3 1
2 3 4
1 3 6
'''

'''
6
1 2 -1 
2 1 -1 
1 3 -1
2 3 -1 
3 1 -1
3 2 -1
'''
