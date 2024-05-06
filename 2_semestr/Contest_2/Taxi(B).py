"""
Алгоритм Диикстры
Перевести км в стоимость
"""
n, A, B, C, d = map(float, input().split())
m = int(input())
def read_graph_as_neigh_list_w():
    edge_list = road
    graph_dict = {}
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
    try:
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
    except:
        return None
road = []
for i in range(m):
    dfr = list(map(float, input().split()))
    road.append(dfr)
    dft = [dfr[1], dfr[0], dfr[-1]]
    road.append(dft)
graph = read_graph_as_neigh_list_w()
if Dijkstra_sum_min(graph, A, C) != None:
    road = [Dijkstra_sum_min(graph, A, B),Dijkstra_sum_min(graph, C, B), Dijkstra_sum_min(graph, C, A)]
    if (road[0]+road[1]-road[2]) != 0:
        print((road[0]+road[1]-road[2])*d)
    else:
        print('0.0')
else:
    print(-1)
"""
class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)
    def construct_graph(self, nodes, init_graph):
        graph = {}
        for node in nodes:
            graph[node] = {}
        graph.update(init_graph)
        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = value
                    graph[node][adjacent_node] = value
        return graph
    def get_nodes(self):
        return self.nodes
    def get_outgoing_edges(self, node):
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections
    def value(self, node1, node2):
        return self.graph[node1][node2]
def dijkstra_algorithm(graph, start_node):
    try:
        unvisited_nodes = list(graph.get_nodes())
        shortest_path = {}
        previous_nodes = {}
        max_value = float('infinity')
        for node in unvisited_nodes:
            shortest_path[node] = max_value
        shortest_path[start_node] = 0
        while unvisited_nodes:
            current_min_node = None
            for node in unvisited_nodes:
                if current_min_node == None:
                    current_min_node = node
                elif shortest_path[node] < shortest_path[current_min_node]:
                    current_min_node = node
            neighbors = graph.get_outgoing_edges(current_min_node)
            for neighbor in neighbors:
                tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
                if tentative_value < shortest_path[neighbor]:
                    shortest_path[neighbor] = tentative_value
                    previous_nodes[neighbor] = current_min_node
            unvisited_nodes.remove(current_min_node)
        return previous_nodes, shortest_path
    except:
        return None
def print_result(previous_nodes, shortest_path, start_node, target_node):
    try:
        path = []
        node = target_node
        while node != start_node:
            path.append(node)
            node = previous_nodes[node]
        path.append(start_node)
        return shortest_path[target_node]
    except:
        return None
n, A, B, C, d = map(float, input().split())
m = int(input())
nodes = []
for i in range(m):
    nodes.append(i+1)
init_graph = {}
for node in nodes:
    init_graph[node] = {}
if len(init_graph)!=0:
    for i in range(m):
        road = list(map(float, input().split()))
        init_graph[road[0]][road[1]] = road[2]
    graph = Graph(nodes, init_graph)
    pom = [A,B,C,A]
    road = []
    Flag = True
    for i in range(3):
        previous_nodes, shortest_path = dijkstra_algorithm(graph=graph, start_node=pom[i])
        road.append(print_result(previous_nodes, shortest_path, start_node=pom[i], target_node=pom[i+1]))
    for i in range(3):
        if road[i] == None:
            print(-1)
            Flag = False
            break
        else:
            continue
    if Flag:
        print((road[0]+road[1]-road[2])*d)
else:
    print(-1)"""
"""
5 1 2 3 4.25
5
1 4 2.5
4 2 3
4 5 3
3 5 2
3 4 8
"""
"""n, a, b, c, cost = map(float, input().split())
n = int(n)
a = int(a-1)
b = int(b-1)
c = int(c-1)
al =[[] for _ in range(n)]
mat = [[1000 for _ in range(n)] for _ in range(n)]
m = int(input())
for i in range(m):
    src, dest, w = map(float, input().split())
    mat[int(src-1)][int(dest-1)] = w * cost
    mat[int(dest - 1)][int(src - 1)] = w * cost
    al[int(src-1)].append(int(dest-1))
    al[int(dest - 1)].append(int(src - 1))

def heapify(array, i):
    parent = i
    left = 2 * i + 2
    right =2 * i + 1
    if left < len(array) and array[left][0] < array[parent][0]:
        parent = left
    if right < len(array) and array[right][0] < array[parent][0]:
        parent = right
    if parent != i:
        array[i], array[parent] = array[parent], array[i]
        heapify(array, parent)
def Sort(array, num):
    array_0 = array[:]
    for i in range(len(array), -1, -1):
        heapify(array, i)
    return array
def dijkstra(n, adj_list, adj_matrix, src):
    BIG_NUM = 1000
    heap = [[0, src]]
    vert_num = n
    dist = [BIG_NUM for _ in range(vert_num)]
    dist[src] = 0
    while heap:
        heap = Sort(heap, 0)
        u = heap[0][1]
        heap.pop(0)
        for v in al[u]:
            if dist[v] > dist[u] + adj_matrix[u][v]:
                dist[v] = dist[u]+  adj_matrix[u][v]
                heap.append([dist[v], v])
    return dist
x1 = dijkstra(n, al, mat, a)[b]
x2 = dijkstra(n, al, mat, b)[c]
x3 = dijkstra(n, al, mat, a)[c]
t = 0
if x1 < 1000 and x2 < 1000 and x3 < 1000:
    res = -x3 + (x1 + x2)
else:
    res = -1
print(res)"""