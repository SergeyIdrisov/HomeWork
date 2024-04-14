"""class Graph:
    def __init__(self, vertex):
        self.V = vertex
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def search(self, parent, i):
        if parent[i] == i:
            return i
        return self.search(parent, parent[i])

    def apply_union(self, parent, rank, x, y):
        xroot = self.search(parent, x)
        yroot = self.search(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.search(parent, u)
            y = self.search(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
        for u, v, weight in result:
            print("Edge:", u, v, end=" ")
            print("-", weight)

m,n = map(int, input().split())
graph = Graph(m)
for i in range(n):
    u, v, w = map(int, input().split())
    graph.add_edge(u-1,v-1,w)
graph.kruskal()"""
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
visited = []
class KruskalMST:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])
    def union(self, parent, rank, x, y):
        x_root = self.find(parent, x)
        y_root = self.find(parent, y)

        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1
    def kruskal(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        return result
def edge_inclusion(n, m, edges):
    kruskal = KruskalMST(n)
    for edge in edges:
        kruskal.add_edge(edge[0], edge[1], edge[2])
    mst = kruskal.kruskal()
    results = []
    for edge in edges:
        kruskal = KruskalMST(n)
        for e in edges:
            if e != edge:
                kruskal.add_edge(e[0], e[1], e[2])
        temp_mst = kruskal.kruskal()
        visited.append(temp_mst)
    return temp_mst
def mainZ():
    n, m = map(int, input().split())
    edges = []
    krusial = KruskalMST(n)
    for _ in range(m):
        a, b, w = map(int, input().split())
        edges.append((a-1, b-1, w))
        krusial.add_edge(a-1, b-1, w)
    temp_mst = edge_inclusion(n, m, edges)
    for edge in krusial.graph:
        a=0
        for i in range(len(visited)):
            if visited[i].count(edge):
                a +=1
        if a == len(visited)-1:
            print('any')
        elif a!=0:
            print('at least one')
        else:
            print('none')
mainZ()